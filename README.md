# Support investigation: The CSV import that reports success but creates no contacts

**Prepared by:** Hazie Herbert  
**Purpose:** Work sample for Growix Technical Support Representative application  
**Important:** This is an original, fictional product-support simulation. It is NOT a Growix customer case, not a claim of prior support employment, and no customer information is included.

## Case summary
A fictional customer reports: “The import says completed, but I can't see any contacts.” The diagnostic hypothesis is an optional UTF-8 byte order mark (BOM) at the start of a CSV file. A naïve CSV reader interprets the first column name as `\ufeffemail` instead of `email`, leading to a validation mismatch. A product that doesn't surface row-level validation failures might appear to succeed while importing no contacts.

## Evidence we can actually reproduce
Run `python3 reproduce.py`. It compares two fictional sample files containing the same record:

- `import_standard.csv`: standard UTF-8, accepted by the minimal local validator.
- `import_bom.csv`: UTF-8 with BOM, fails the minimal local validator because `email` is missing.

This demonstrates a plausible parser edge case. It **does not demonstrate that any real Growix client's product has this bug**.

## Support judgment
1. Acknowledge and ask permission to inspect the import job; do not request raw customer contact records in email.
2. Confirm workspace, user permissions, file size, import job ID, timestamp/timezone, field mapping, and whether a result summary exists.
3. Ask the customer to retry a minimal non-sensitive file saved as UTF-8 (no BOM) only if safe; give a workaround without promising a fix.
4. If engineering investigation is needed, supply a redacted CSV fixture, reproduction steps, expected/actual, impact, and what is confirmed versus hypothesised.
5. Close the loop with a public-facing knowledge-base note and product improvement proposal: detect the BOM, expose row-level errors, and never report success for zero accepted records without explaining why.

The accompanying PDF has the customer message, L2 escalation, help-centre article, and prevention proposal.
