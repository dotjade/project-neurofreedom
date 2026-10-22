# Okun 2024 clinical/function estimand audit

The [report](report.md) separates primary-outcome-period video states, longitudinal recalled tic severity and MOS-36 function. The functional comparative-effect calculation stops at missing public aggregate prerequisites; nonsignificance is not equivalence or proof of no benefit.

## Reproduce the documentation checks

From this directory, with Python 3 and the standard library:

```sh
PYTHONDONTWRITEBYTECODE=1 python check_extraction.py
```

The check reads the saved server-projected registry metadata and original structured extraction, verifies identities/counts/windows and rejects measurement payloads. It writes `checks.json` with execution time and hashes. Add `--no-write` to validate without changing the archived check record. The checks do not reproduce a clinical effect, perform a hypothesis test or use participant data. A deliberately malformed synthetic dictionary tests only the metadata parser's rejection boundary, not biology.

An optional fresh source retrieval is separate from offline reproduction:

```sh
python collect_registry_metadata.py
```

This uses an explicit official ClinicalTrials.gov field projection excluding all measurement classes/categories. A new registry response can differ; date and review it rather than pretending it is the archived snapshot. Paper and protocol source bytes are not archived. URLs, initial access outcomes and response hashes are in `source-retrieval.json`; original methods decisions are in `structured-extraction.json` and `provenance.json`.

The canonical evidence addition is `evidence-record.jsonl` with ID `pmid:38499664`, linked to overlapping Cagle 2022/NCT02056873. The [independent review](review/independent_review.md) is a source/inference check, not clinical peer review. No participant rows, case narratives, recordings or unlicensed full texts are included.
