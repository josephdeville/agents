# Refined signal spec

"Hiring an SDR" is too broad. A good signal shows (1) they need what we sell, (2) they can pay, (3) it is urgent now, and (4) they are small enough to buy from a freelancer.

## The four signals
| | Signal | Why it matters | Source |
|---|---|---|---|
| A | Open role in last 30 days: GTM Engineer, RevOps, Sales Ops, Growth Ops, Founding SDR, first sales hire | They need the skill we sell. Pitch it as a contract that starts before a hire could. | Job post (Ashby, Greenhouse, Lever, Workable) |
| B | Seed to Series B round in last 120 days | Budget and a deadline to show pipeline | Funding event with source URL |
| C | Job post names tools we build in: Clay, HubSpot, Salesforce, Apollo, Instantly, Outreach, Salesloft | The stack exists, so Jev scoring and reply triage plug in | The job post text |
| D | 10-150 employees, US | Small enough to buy from a freelancer | Company profile |

## Tiers
- **Tier A (contact this week):** D plus at least two of A, B, C.
- **Tier B (queue):** D plus one of A, B, C.
- **Drop:** more than 200 staff; sells sales, outbound or revenue software; agency or staffing firm; 4+ open sales roles (already has a team); posting older than 30 days.

Every signal needs a source URL and a date. A signal with no source counts as absent.

## What the first refined run found (Exa agent, $0.025, Oct 6)
| Company | Staff | Signals | Verdict |
|---|---|---|---|
| **Infera** | 15 | A (Founding SDR, posted 2026-09-16), C (Apollo, Clay, Dripify, Attio named in post) | **Pass (Oct 7).** On the do-not-contact list; weak fit (tooling already built, "No AI SDR. No agency." post); the SDR role may be closed. One LinkedIn DM was sent by mistake on Oct 7. Funding was never verified. Do not follow up. |
| Zania | 23 | A, C (Clay named) | **Dropped.** The agent called the post "within 30 days"; it was posted 2026-08-12, about 55 days before this run. |

Lessons:
- Stricter signals gave 2 matches instead of 5, and one failed my own date check. **Always recompute the post age in code, never trust the agent's summary.**
- Funding (B) returned nothing at low effort. Use PredictLeads for B and for tech detection (it has financing events, job openings and technology detections), and keep Exa for discovery.
- The agent's grounding also surfaced three more candidates it did not return, unverified: Clera ("Founding GTM"), Surface Labs ("Founding GTM (SDR)", via Work at a Startup), and Unikraft ("GTM Engineer"; likely not a US company). Check these before dropping them.

## Rules for any run
1. Estimate cost, state it, then run. Exa agent at `low` effort (about $0.025 per run) until the signal is proven.
2. After each run, recompute dates and employee counts in code; flag any signal older than its window.
3. Log every company and which signals matched in `ledger.csv`.
4. A company enters outreach only at Tier A, with one verified, dated fact to open on.
