"""Reproduce a UTF-8 BOM CSV header mismatch using Python's standard library.
This is a standalone simulation, not a Growix client application.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQUIRED = {'email', 'name'}

for filename in ('import_standard.csv', 'import_bom.csv'):
    with (ROOT / filename).open('r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames or []
        rows = list(reader)
    missing = sorted(REQUIRED - set(headers))
    print(f'{filename}: headers={headers!r}; rows={len(rows)}; missing={missing!r}; valid={not missing}')

print('Fix: open with encoding="utf-8-sig" to strip an optional BOM.')
