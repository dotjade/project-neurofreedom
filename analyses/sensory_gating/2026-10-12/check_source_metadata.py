#!/usr/bin/env python3
"""Audit public identifiers/access metadata without saving abstract or full text.

Not an effect-size analysis. No participant data, numerical effect estimates,
or confidence intervals are created. Python standard library only.
"""
import datetime as dt
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
DOI = "10.1016/j.biopsycho.2026.109408"
PMID = "42810670"
URLS = {
    "pubmed": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42810670&retmode=xml",
    "crossref": "https://api.crossref.org/works/10.1016%2Fj.biopsycho.2026.109408",
    "pubmed_to_pmc": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pmc&id=42810670&retmode=json",
    "openalex": "https://api.openalex.org/works/https://doi.org/10.1016/j.biopsycho.2026.109408",
}


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def retrieve(name, url):
    result = {"source": name, "url": url, "retrieved_at_utc": now()}
    try:
        with urlopen(url, timeout=40) as response:
            body = response.read()
            result.update(http_status=response.status,
                          retrieved_body_sha256=hashlib.sha256(body).hexdigest(),
                          retrieved_body_bytes=len(body))
        if name == "pubmed":
            root = ET.fromstring(body)
            abstract = " ".join("".join(x.itertext()) for x in root.findall(".//AbstractText"))
            result["extraction"] = {
                "pmid": root.findtext(".//MedlineCitation/PMID"),
                "title": root.findtext(".//ArticleTitle"),
                "electronic_publication_date": {x.tag: x.text for x in root.findall(".//ArticleDate/*")},
                "record_revised_date": {x.tag: x.text for x in root.findall(".//DateRevised/*")},
                "identifiers": {x.attrib["IdType"]: x.text for x in root.findall(".//ArticleIdList/ArticleId")},
                "volume": root.findtext(".//JournalIssue/Volume"),
                "linked_comments_corrections": [{"relation": x.attrib, "pmid": x.findtext("PMID"), "source": x.findtext("RefSource")} for x in root.findall(".//CommentsCorrections")],
                "gating_difference_term_present": "gating differences" in abstract,
                "regression_marginal_effect_term_present": "regression analysis marginal effects" in abstract,
                "copyright_statement": root.findtext(".//CopyrightInformation"),
            }
            assert result["extraction"]["identifiers"]["doi"] == DOI
            assert result["extraction"]["pmid"] == PMID
        elif name == "crossref":
            record = json.loads(body)["message"]
            assert record["DOI"] == DOI
            result["extraction"] = {k: record.get(k) for k in ["DOI", "title", "volume", "published-print", "created", "deposited", "license", "link", "resource", "relation", "update-to", "funder"]}
        elif name == "pubmed_to_pmc":
            result["extraction"] = json.loads(body)
        else:
            record = json.loads(body)
            assert record["doi"] == "https://doi.org/" + DOI
            result["extraction"] = {
                "id": record["id"], "doi": record["doi"],
                "publication_date": record.get("publication_date"),
                "open_access": record.get("open_access"),
                "locations": [{k: location.get(k) for k in ["landing_page_url", "pdf_url", "license", "version", "is_oa"]} for location in record.get("locations", [])],
            }
        result["status"] = "metadata_retrieved"
    except Exception as error:
        result["status"] = "retrieval_or_validation_failed"
        result["error"] = f"{type(error).__name__}: {error}"
    print(json.dumps({k: result[k] for k in ["source", "status", "retrieved_at_utc"]}), flush=True)
    return result


def main():
    output = {
        "created_at_utc": now(),
        "kind": "metadata_access_audit_not_statistical_reanalysis",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "sources": [retrieve(name, url) for name, url in URLS.items()],
        "effect_or_precision_calculation_executed": False,
        "reason": "Available abstract lacks estimates, sampling uncertainty, outcome-specific denominators, and sufficient model specification. Sample counts alone cannot recover precision.",
        "stored_source_material": "Selected bibliographic and access metadata only; no abstract or paper full text saved.",
    }
    path = HERE / "source_metadata.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print("Wrote " + path.name, flush=True)


if __name__ == "__main__":
    main()
