#!/usr/bin/env python3
"""SYNTHETIC methods benchmark, arbitrary units. No patient inputs or clinical inference."""
import argparse
import csv
from functools import lru_cache
import hashlib
import json
import os
from pathlib import Path
import platform
os.environ.setdefault('MPLCONFIGDIR', '/tmp/neurofreedom-matplotlib')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SEED = 20261008
HISTORIES = (96, 192, 384)
HORIZON = 48
PERIODS = np.arange(24., 96.01, .5)
SCENARIOS = ('fixed_period', 'autocorrelated', 'slow_trend', 'reporting_noise',
             'noisy_fixed_period', 'drifting_period', 'periodic_reporting_bias')
LABELS = ('Fixed period + noise', 'Autocorrelated, no oscillator', 'Slow trend + correlated noise',
          'Reporting noise, no oscillator', 'Fixed period, noisier reporting',
          'Drifting-period oscillator', 'Periodic reporting bias')
BASELINES = ('mean', 'linear', 'ar1', 'detrended_ar1', 'recent_mean', 'persistence')


def ar1(rng, n, rho):
    """Stationary AR(1), marginal variance one."""
    x = np.empty(n)
    x[0] = rng.normal()
    e = rng.normal(size=n-1) * np.sqrt(1-rho*rho)
    for j in range(1, n):
        x[j] = rho*x[j-1]+e[j-1]
    return x


def generate(scenario, rep, seed=SEED, n=432):
    """Independent RNG per replicate; matched innovations across scenarios."""
    rng = np.random.default_rng(np.random.SeedSequence([seed, rep]))
    t = np.arange(n, dtype=float)
    phase = rng.uniform(0, 2*np.pi)
    a, b = ar1(rng, n, .85), ar1(rng, n, .94)
    e = rng.normal(size=n)
    drift, wave = .0025*t, 1.5*np.sin(2*np.pi*t/48+phase)
    bias = np.zeros(n)
    if scenario == 'fixed_period':
        latent, error = drift+.45*a+wave, .6*e
    elif scenario == 'periodic_reporting_bias':
        latent, error, bias = drift+.45*a, .6*e, wave
    elif scenario == 'autocorrelated':
        latent, error = drift+1.3*b, .6*e
    elif scenario == 'slow_trend':
        latent, error = .012*t+.55*a, .6*e
    elif scenario == 'reporting_noise':
        latent, error = drift, 1.5*e
    elif scenario == 'noisy_fixed_period':
        latent, error = drift+.45*a+wave, 1.8*e
    elif scenario == 'drifting_period':
        angle = phase+(2*np.pi/.10)*np.log((36+.10*t)/36)
        latent, error = drift+.45*a+1.5*np.sin(angle), .6*e
    else:
        raise ValueError(scenario)
    # Parentheses preserve exact equality in the deliberately nonidentifiable pair.
    return dict(time=t, latent=latent, report_bias=bias, observed=(latent+bias)+error)


def design(t, n, period=None):
    cols = [np.ones(len(t)), (t-(n-1)/2)/n]
    if period is not None:
        cols += [np.sin(2*np.pi*t/period), np.cos(2*np.pi*t/period)]
    return np.column_stack(cols)


@lru_cache(maxsize=None)
def harmonic_design(n):
    # Cache depends only on time coordinates, never observations.
    x = np.stack([design(np.arange(n), n, p) for p in PERIODS])
    return x, np.linalg.pinv(x)


def fit_harmonic(y, horizon=HORIZON):
    x, inv = harmonic_design(len(y))
    coef = np.einsum('pkn,n->pk', inv, y)
    fits = np.einsum('pnk,pk->pn', x, coef)
    sses = np.sum((fits-y)**2, axis=1)
    i = int(np.argmin(sses))
    period = float(PERIODS[i])
    forecast = design(np.arange(len(y), len(y)+horizon), len(y), period) @ coef[i]
    return forecast, period, float(sses[i]), fits[i]


def fit_baseline(y, model, horizon=HORIZON):
    n = len(y)
    if model == 'mean':
        return np.full(horizon, np.mean(y))
    if model == 'recent_mean':
        return np.full(horizon, np.mean(y[-12:]))
    if model == 'persistence':
        return np.full(horizon, y[-1])
    x = design(np.arange(n), n)
    coef = np.linalg.lstsq(x, y, rcond=None)[0]
    line = design(np.arange(n, n+horizon), n) @ coef
    if model == 'linear':
        return line
    if model in ('ar1', 'detrended_ar1'):
        center = x @ coef if model == 'detrended_ar1' else np.full(n, np.mean(y))
        r = y-center
        rho = np.clip((r[:-1] @ r[1:])/max(float(r[:-1] @ r[:-1]), 1e-12), 0, .995)
        equilibrium = line if model == 'detrended_ar1' else np.full(horizon, np.mean(y))
        return equilibrium+rho**np.arange(1, horizon+1)*r[-1]
    raise ValueError(model)


def inner_origins(n, horizon=HORIZON):
    cuts = [c for c in (n-2*horizon, n-horizon) if c >= 48]
    if not cuts:
        raise ValueError('Insufficient history')
    return cuts


def predict_from_history(y, horizon=HORIZON):
    """The outer future cannot enter this API; all selection is past-only."""
    y = np.asarray(y, dtype=float)
    if y.ndim != 1 or not np.isfinite(y).all():
        raise ValueError('Only finite, regularly sampled 1-D histories are supported')
    scores = {m: [] for m in BASELINES+('harmonic',)}
    for cut in inner_origins(len(y), horizon):
        past, val = y[:cut], y[cut:cut+horizon]
        for m in BASELINES:
            scores[m].append(float(np.mean((fit_baseline(past, m, horizon)-val)**2)))
        scores['harmonic'].append(float(np.mean((fit_harmonic(past, horizon)[0]-val)**2)))
    cv = {m: float(np.mean(v)) for m, v in scores.items()}
    chosen = min(BASELINES, key=cv.get)
    harmonic, period, sse, fitted = fit_harmonic(y, horizon)
    baseline = fit_baseline(y, chosen, horizon)
    x = design(np.arange(len(y)), len(y))
    line_sse = float(np.sum((y-x @ np.linalg.lstsq(x, y, rcond=None)[0])**2))
    p1 = fit_harmonic(y[:len(y)//2], horizon)[1]
    p2 = fit_harmonic(y[len(y)//2:], horizon)[1]
    stable = abs(p1-p2)/((p1+p2)/2) <= .10 and all(PERIODS[0]<p<PERIODS[-1] for p in (p1, p2))
    choose_h = cv['harmonic'] < cv[chosen]
    # A line already explains a constant/linear history to floating precision.
    # Do not manufacture a unit fit gain by dividing two near-zero residuals.
    sse_tolerance = 100*np.finfo(float).eps*max(1.0, float(np.sum(y*y)))
    fit_gain = 0.0 if line_sse <= sse_tolerance else float(np.clip(1-sse/line_sse, 0.0, 1.0))
    return dict(harmonic=harmonic, baseline=baseline, selected=harmonic if choose_h else baseline,
                fitted=fitted, period=period, baseline_model=chosen, fit_gain=fit_gain,
                inner_harmonic_selected=choose_h, period_stable_halves=stable,
                first_half_period=p1, second_half_period=p2, inner_cv_mse=cv)


def aggregate(rows, seed):
    rng = np.random.default_rng(seed+1)
    count = sum(r['scenario']==SCENARIOS[0] and r['history']==HISTORIES[0] for r in rows)
    ids = rng.integers(0, count, size=(2000, count))
    output = []
    for scenario in SCENARIOS:
        for n in HISTORIES:
            rr = [r for r in rows if r['scenario']==scenario and r['history']==n]
            h, b = (np.array([r[k] for r in rr]) for k in ('harmonic_mse', 'baseline_mse'))
            # Resample trajectories, never dependent individual time points.
            bs = 1-np.mean(h[ids], axis=1)/np.mean(b[ids], axis=1)
            low, high = np.quantile(bs, [.025, .975])
            d = dict(scenario=scenario, history=n, replicates=len(rr), harmonic_mse_mean=float(np.mean(h)),
                     baseline_mse_mean=float(np.mean(b)), selected_mse_mean=float(np.mean([r['selected_mse'] for r in rr])),
                     harmonic_skill=float(1-np.mean(h)/np.mean(b)), skill_ci_low=float(low), skill_ci_high=float(high),
                     harmonic_oos_win_rate=float(np.mean(h<b)))
            for model in BASELINES:
                d['fixed_'+model+'_mse_mean'] = float(np.mean([r['fixed_'+model+'_mse'] for r in rr]))
            line = np.array([r['fixed_linear_mse'] for r in rr])
            line_bs = 1-np.mean(h[ids], axis=1)/np.mean(line[ids], axis=1)
            line_lo, line_hi = np.quantile(line_bs, [.025, .975])
            d.update(skill_vs_linear=float(1-np.mean(h)/np.mean(line)), linear_skill_ci_low=float(line_lo), linear_skill_ci_high=float(line_hi))
            for dest, source in [('apparent_cycle_rate', 'apparent_cycle'), ('inner_harmonic_selection_rate', 'inner_harmonic_selected'),
                                 ('stable_half_period_rate', 'period_stable_halves')]:
                d[dest] = float(np.mean([r[source] for r in rr]))
            d['period_recovery_rate'] = float(np.mean([r['period_recovered'] for r in rr])) if scenario in (SCENARIOS[0], SCENARIOS[4], SCENARIOS[6]) else None
            output.append(d)
    return output


def write_csv(path, rows):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def make_plots(rows, summary, out, seed):
    plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})
    fig, axes = plt.subplots(1, 2, figsize=(13.4, 5.7))
    for scenario, label in zip(SCENARIOS[:-1], LABELS[:-1]):
        rr = [r for r in summary if r['scenario']==scenario]
        x = np.array([r['history'] for r in rr])
        line = axes[0].plot(x, [100*r['apparent_cycle_rate'] for r in rr], marker='o', label=label)[0]
        y = np.array([100*r['harmonic_skill'] for r in rr])
        lo, hi = (np.array([100*r[k] for r in rr]) for k in ('skill_ci_low', 'skill_ci_high'))
        axes[1].errorbar(x, y, yerr=[y-lo, hi-y], marker='o', capsize=3, color=line.get_color())
    axes[0].set(ylabel='Apparent-cycle flag (%)', title='In-sample fit can look rhythmic', ylim=(-2, 102))
    axes[1].set(ylabel='Held-out MSE improvement (%)', title='Future gain vs. past-selected nonperiodic baseline')
    axes[1].axhline(0, color='black', lw=.8)
    for ax in axes:
        ax.set_xticks(HISTORIES)
        ax.set_xlabel('Training-history length (arbitrary time steps)')
        ax.grid(alpha=.2)
    fig.suptitle('SYNTHETIC benchmark: apparent fit versus future prediction', fontsize=14)
    fig.legend(*axes[0].get_legend_handles_labels(), loc='lower center', ncol=3, frameon=False)
    fig.text(.5, .105, 'Positive skill favors harmonic forecast; bars: 95% bootstrap intervals across synthetic replicates.', ha='center', fontsize=9)
    fig.tight_layout(rect=(0, .15, 1, .94))
    fig.savefig(out/'benchmark.png', dpi=180)
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    for scenario, label in zip(SCENARIOS[:-1], LABELS[:-1]):
        rr = [r for r in summary if r['scenario']==scenario]
        y = np.array([100*r['skill_vs_linear'] for r in rr])
        lo, hi = (np.array([100*r[k] for r in rr]) for k in ('linear_skill_ci_low', 'linear_skill_ci_high'))
        ax.errorbar(HISTORIES, y, yerr=[y-lo, hi-y], marker='o', capsize=3, label=label)
    ax.axhline(0, color='black', lw=.8)
    ax.set(title='SYNTHETIC comparator sensitivity: harmonic vs. fixed linear trend', xlabel='Training-history length (arbitrary steps)', ylabel='Held-out MSE improvement (%)')
    ax.set_xticks(HISTORIES)
    ax.grid(alpha=.2)
    ax.legend(fontsize=9, loc='lower right')
    fig.tight_layout()
    fig.savefig(out/'comparator_sensitivity.png', dpi=180)
    plt.close(fig)
    examples = []
    for scenario in SCENARIOS[:2]:
        rr = [r for r in rows if r['scenario']==scenario and r['history']==96]
        if scenario == 'autocorrelated':
            bad = [r for r in rr if r['apparent_cycle'] and r['harmonic_mse']>r['baseline_mse']]
            choice, reason = (bad or rr)[0], 'First apparent-cycle flag with worse future harmonic error (illustration selected to show failure)'
        else:
            choice, reason = rr[0], 'First replicate; no performance selection'
        examples.append(dict(scenario=scenario, replicate=choice['replicate'], selection=reason))
    fig, axes = plt.subplots(2, 2, figsize=(13.5, 7.6), sharey='row')
    for row, ex in enumerate(examples):
        data = generate(ex['scenario'], ex['replicate'], seed)
        for col, n in enumerate((96, 384)):
            pred = predict_from_history(data['observed'][:n])
            stop, ax = n+HORIZON, axes[row, col]
            ax.plot(data['time'][:stop], data['observed'][:stop], color='.55', alpha=.65, lw=.8, label='Synthetic observation')
            ax.plot(np.arange(n), pred['fitted'], color='#2878b5', lw=1.3, label='Harmonic training fit')
            ax.plot(np.arange(n, stop), pred['harmonic'], color='#2878b5', lw=2, ls='--', label='Harmonic future forecast')
            ax.plot(np.arange(n, stop), pred['baseline'], color='#db651d', lw=2, ls='--', label='Past-selected baseline forecast')
            ax.axvline(n-.5, color='black', lw=.8)
            ax.axvspan(n-.5, stop, color='#e9f1e4', alpha=.6)
            ax.set(title=f"{LABELS[SCENARIOS.index(ex['scenario'])]}; history={n}; fitted P={pred['period']:.1f}",
                   xlabel='Arbitrary time step', ylabel='Arbitrary synthetic score')
    fig.suptitle('SYNTHETIC examples: green region withheld from model fitting and model selection', fontsize=13)
    fig.legend(*axes[0, 0].get_legend_handles_labels(), loc='lower center', ncol=2, frameon=False)
    fig.tight_layout(rect=(0, .075, 1, .95))
    fig.savefig(out/'examples.png', dpi=180)
    plt.close(fig)
    return examples


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replicates', type=int, default=240)
    parser.add_argument('--seed', type=int, default=SEED)
    parser.add_argument('--out', type=Path, default=Path(__file__).resolve().parent/'outputs')
    args = parser.parse_args()
    if args.replicates < 2:
        parser.error('Use at least two replicates')
    args.out.mkdir(parents=True, exist_ok=True)
    rows = []
    for scenario in SCENARIOS:
        for rep in range(args.replicates):
            data = generate(scenario, rep, args.seed)
            for n in HISTORIES:
                pred = predict_from_history(data['observed'][:n])
                future = data['observed'][n:n+HORIZON]
                r = dict(scenario=scenario, replicate=rep, history=n, forecast_horizon=HORIZON,
                         period=pred['period'], baseline_model=pred['baseline_model'], fit_gain=pred['fit_gain'],
                         apparent_cycle=pred['fit_gain']>=.25, inner_harmonic_selected=pred['inner_harmonic_selected'],
                         period_stable_halves=pred['period_stable_halves'], first_half_period=pred['first_half_period'],
                         second_half_period=pred['second_half_period'],
                         period_recovered=abs(pred['period']-48)/48<=.10 if scenario in (SCENARIOS[0], SCENARIOS[4], SCENARIOS[6]) else None)
                for model in ('harmonic', 'baseline', 'selected'):
                    r[model+'_mse'] = float(np.mean((pred[model]-future)**2))
                for model in BASELINES:
                    r['fixed_'+model+'_mse'] = float(np.mean((fit_baseline(data['observed'][:n], model)-future)**2))
                rows.append(r)
        print(f'Completed {scenario}: {args.replicates} synthetic trajectories', flush=True)
    summary = aggregate(rows, args.seed)
    write_csv(args.out/'replicate_results.csv', rows)
    write_csv(args.out/'summary.csv', summary)
    examples = make_plots(rows, summary, args.out, args.seed)
    metadata = dict(warning='SYNTHETIC methods validation only; no patient data; not a biological result or medical device.',
                    seed=args.seed, replicates_per_scenario=args.replicates, history_lengths=HISTORIES, forecast_horizon=HORIZON,
                    period_grid=dict(min=24, max=96, step=.5), apparent_cycle_threshold=.25, bootstrap_resamples=2000,
                    fixed_true_period=48, time_units='arbitrary synthetic steps', example_selection=examples,
                    versions=dict(python=platform.python_version(), numpy=np.__version__, matplotlib=matplotlib.__version__),
                    same_replicate_across_histories_and_scenarios_is_paired=True, independent_unit_for_bootstrap='replicate trajectory',
                    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (args.out/'metadata.json').write_text(json.dumps(metadata, indent=2)+'\n')
    (args.out/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print('\nScenario | history | apparent flag | forecast skill [95% Monte Carlo CI]')
    for r in summary:
        print(f"{r['scenario']:25s} {r['history']:3d} {r['apparent_cycle_rate']:6.1%} {r['harmonic_skill']:7.1%} [{r['skill_ci_low']:.1%}, {r['skill_ci_high']:.1%}]")


if __name__ == '__main__':
    main()
