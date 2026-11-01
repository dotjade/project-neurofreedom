"""Offline editorial checks. Run: python updates/2026-11-01-monthly/validate.py"""
from pathlib import Path
import re, json
root = Path(__file__).resolve().parent
text = (root / "report.md").read_text()
checks = 0
for prefix, maximum in (("H", 20), ("C", 8)):
    for i in range(1, maximum + 1):
        label = f"H{i:02}" if prefix == "H" else f"C{i}"
        assert len(re.findall(r"^\| " + label + r" ", text, re.M)) == 1, label
        checks += 1
assert "\u2014" not in text
assert "not a new simulation or patient-data computation" in text
rows = json.loads((root / "portfolio.json").read_text())["rows"]
assert len(rows) == 20 and all(len(row) == 4 for row in rows)
checks += 3
print(f"{checks} editorial structure checks passed; not clinical validation")
