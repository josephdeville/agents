# Jev request templates for Clay

The setup details come from the GTM Engineering newsletter (Sept 28). They haven't been tested against the live API yet, so check them in TypeSafe's Playground first.

## HTTP API column
- **Method:** POST
- **URL:** `https://api.typesafe.ai/v1/systemone`
- **Headers:**
  - `Authorization: Bearer <TYPESAFE_API_KEY>`
  - `Content-Type: application/json`
- **Body:** one of the `.json` files here. Swap `{{...}}` for Clay column tokens and `[BRACKETS]` for the client's details.

| File | Use | Offer |
|------|-----|-------|
| persona_icp.json | Persona plus ICP fit in one call | A, B |
| title_score.json | Score unique job titles (cheap first pass) | B, C |
| buyer_map_5to1.json | Full-profile 5→1 buyer score | C |
| reply_triage.json | Classify cold-email replies | D |
| inbound_routing.json | Route form fills | D |
| hiring_signal.json | Job post as a buying signal | D |

## Response fields to extract
- choice: `answers.<q>.choice`, `answers.<q>.confidence`
- score: `answers.<q>.score` (a weighted average such as 2.6, so round it), `answers.<q>.confidence`
- noul: a probability between 0 and 1. Check the exact field name in the Playground.

## Lane formula (Clay formula column)
```
{{confidence}} >= 0.9 ? "auto" : ({{confidence}} >= 0.7 ? "review" : "hold")
```
Use stricter thresholds for actions that are hard to undo, such as enrolling someone in a sequence.

## Rules that keep accuracy up
1. Keep the state short and labeled. Include only what a smart human would need. Never paste the whole enrichment blob (64K token cap, and more context lowers accuracy).
2. Every choice question gets an `unclear` option.
3. Criteria must not overlap ("Enterprise" vs "Large company" is a bug).
4. Add a run condition: only run when the input fields aren't empty.
5. Merged fields with `"` or line breaks cause 422 errors. Clean them in a formula column first.
6. 429 or 529 means lower the column's rate limit and retry.
7. Start with 50 rows and hand-label 20. When it's wrong, look at the second-highest probability and rewrite the criteria.
