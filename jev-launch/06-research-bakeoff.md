# Research bake-off: Exa vs Perplexity

Same question to both, so the comparison is fair: 5 US B2B software companies (20-200 staff) with an open SDR/BDR/founding-sales role posted in the last 14 days, with job URL, date, sales lead, and a source for every fact.

## Exa agent (run Oct 4)
- Effort: low. Cost: **$0.025** (3 searches).
- Returned 5 companies with job URL, posted date, sales lead and sources per row, plus per-field grounding.
- Spot-checked 2 job posts against the live pages: Middesk (2026-09-23) and INGENIOUS.BUILD (2026-09-22) both correct.
- Companies: INGENIOUS.BUILD, Amigo AI, AISLE, Middesk, Camber. None are sales-tooling vendors, which was the failure of the earlier plain Exa search.
- Caveat: "sales lead" is the CEO in all five. That is useful for a founder-led first touch but is not a head of sales. AISLE's job source is a job aggregator, not the company's own page.

## Perplexity
Run `perplexity_brief.py` with your own key (not run yet; no key in this environment). Start with `sonar-pro`; try `sonar-deep-research` only if the first result is weak.

## Score each result (0-2 per line, 10 lines)
1. Job post exists at the URL (open the link)
2. Posted date matches the page and is within 14 days
3. Company is 20-200 staff and US
4. Not a sales-tool vendor, agency, or job board
5. "What they sell" matches the company website
6. Named sales lead matches a public source
7. Every fact has a source URL
8. Nothing invented (null where unknown)
9. Cost for the 5 rows
10. Time to result

Decision rule: the cheaper tool wins unless it scores 3+ points lower on lines 1-8.

## Credit rules
- Exa: stay at `low` effort; add `budget.maxCostDollars` on any `auto`/`ultra` run.
- Perplexity ($50): `sonar-pro` first; deep research only for the final 25-account briefs; check the `usage` block after every run and log it in the ledger.
- No batch runs until one 5-row run from each tool has been scored.
