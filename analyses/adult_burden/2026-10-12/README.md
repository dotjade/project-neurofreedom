# Adult registry endpoint audit

12 October 2026 | Published aggregate evidence only

Start with [report.md](report.md). The audit checks whether Calgary/Paris registry publications support using tic severity as a burden surrogate or estimating persistent severe adult outcomes. It does not analyze participant records or estimate a treatment effect.

## Files

- [prespecified_question.md](prespecified_question.md): prediction, disconfirming results and bounded method recorded before opening the primary leads
- [extraction.json](extraction.json): original source-level extraction, including unknown fields and cohort-overlap cautions
- [provenance.json](provenance.json): required repository versions, exact searches, source URLs and retrieval limitations
- [aggregate_checks.py](aggregate_checks.py): deterministic count arithmetic and implementation checks
- [aggregate_checks.json](aggregate_checks.json): actual generated results

## Reproduce the arithmetic

From this directory, run:

    python aggregate_checks.py

Python 3's standard library is sufficient; there are no package, network or participant-data dependencies. The computation is deterministic, so no random seed is needed. The command prints the results and overwrites aggregate_checks.json beside the script. Copy the existing output first if preserving it is important.

The completed run passed 47 check groups: 33 feasible attendance-overlap partitions, four boundary cases, five source-count partitions and five final arithmetic checks. A repeat run reproduced the output byte-for-byte. These are implementation/arithmetic checks, not independent clinical validation, statistical evidence or independent review of the source extraction.

## Exact source inputs

Inputs are explicit constants in the script and are traced in extraction.json:

- [Pringsheim and Martino, Results](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mdc3.14296): 95 enrolled adults; 63 and 55 completed six- and twelve-month visits at analysis; diagnostic counts 81/13/1.
- [Nilles et al., Table 1, publisher PDF page 3](https://onlinelibrary.wiley.com/doi/pdf/10.1111/ene.70252): 227 adults; diagnostic counts 210/16/1; sex counts 82/145; nationality counts 108/119; comorbidity denominators 218 overall and 78/140 by sex; antipsychotic counts printed as 95 overall and 33/66 by sex.

The script deliberately preserves the inconsistent antipsychotic inputs rather than correcting them. The attendance intersection is bounded by max(0, 63+55−95) and min(63,55), conditional on both groups belonging to the same 95 enrollees. Completion fractions are not verified retention rates among adults already due for follow-up. Attendance overlap is not proof of complete outcome records or severe persistence.

No source full text is redistributed. Source retrieval and visual-verification limitations are documented in the report and provenance file.
