# Adult tic-related pain audit — 17 October 2026

Read [report.md](report.md) for findings and limits. This historical primary-source audit separates present/worst pain and care denominators. It does not estimate causal efficacy, representative prevalence or a severe-adult subgroup.

- [Prospective question](prespecified_question.md)
- [Structured extraction](extraction.json)
- [Primary evidence record](evidence.jsonl)
- [Source provenance](provenance.json)
- [Aggregate inputs](aggregate_inputs.json), [code](aggregate_checks.py), [output](aggregate_checks.json)
- [18 implementation tests](test_aggregate_checks.py) and [execution log](execution_log.txt)

Reproduce with Python 3 standard library: `python aggregate_checks.py`, then `python -m unittest -v test_aggregate_checks.py`.

Original aggregates and commentary only. No full paper, raw participant data, individual quotations, intervention or outreach. Independent review is linked by the publication workflow.
