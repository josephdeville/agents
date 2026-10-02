# Upwork kit

Nothing here has been submitted or changed on Upwork. Review and paste it yourself, or tell me which pieces to submit.

## 1. Profile updates
**Headline (current):** GTM & RevOps Engineer | Certified HubSpot + Salesforce Admin | Clay
**Headline (proposed):** GTM Engineer | Clay + AI Scoring (Jev) | HubSpot & Salesforce Certified

**Add as the second paragraph of the overview:**
> NEW: I build Clay workflows on Jev, TypeSafe's new decision model. It returns a typed answer (a label, a score, or yes/no) plus a calibrated confidence, at a fraction of an LLM column's cost. I use it for ICP scoring, persona classification, reply triage, and routing, and keep LLM columns for writing only. If your Clay bill is mostly AI columns making yes/no calls, I can usually cut it sharply and show you the side-by-side before you switch.

**Skills to add if available:** Artificial Intelligence, Lead Qualification, Data Enrichment.

**Project Catalog listing**
- **Title:** "I will cut your Clay AI credit spend by moving scoring to Jev"
- **Tiers:**
  - $750: audit + 3 columns rebuilt
  - $1,500: full table + lanes + side-by-side report
  - $3,000: up to 3 tables + Loom training

## 2. Proposals for live jobs

### a) "Clay Specialist for Account Qualification": manufacturers/OEMs, Canada
URL: https://www.upwork.com/jobs/~022099954917376622359

Fit is close to perfect. Caveat: the client already has 1 hire on this post. Cost is 20 Connects.

> You already have ICP criteria, qualification prompts, and hand-reviewed examples, which is exactly what calibration needs. Here's how I'd run the paid test:
>
> 1. Turn your qualification prompts into fixed-answer questions: product category (choice), manufacturing activity (yes/no), equipment complexity (score 1–4), trade-show relevance (yes/no), and overall ICP fit (score). Each gets an "unclear" option so thin records don't get forced into a bucket.
> 2. Score your hand-reviewed examples first and report agreement per question. Where it disagrees, I fix the criteria wording, not the data.
> 3. Gate enrichment on the result: only accounts above the fit threshold get contact enrichment. That's where most of the Clay credit savings come from.
>
> For the classification step I'd use Jev, a new decision model that returns a label plus a calibrated confidence at a small fraction of an LLM column's cost. Your current prompt column stays in place as a fallback.
>
> Clay: end-to-end implementations, Clay Automated Outbound certified, enrichment pipelines running at 10,000+ leads/month. Happy to start with a 100-account calibration batch.
>
> — Joseph

**Screening answers**
- *Clay experience:* "Multiple end-to-end Clay builds: signal-stacked prospecting, waterfall enrichment, scoring, territory routing, CRM sync. Clay Automated Outbound certified."
- *Similar projects:* "Built enrichment pipelines processing 10,000+ leads/month (still running) and a 63,000-record enriched contact base feeding Salesforce. Most recently: scoring and gating logic so expensive enrichment only runs on qualified accounts."

### b) "Clay Expert for Data Prep": optimizing Claygents and credits, US
URL: https://www.upwork.com/jobs/~022099428729913421464

$15–30/hr is low and they already have 1 hire. Apply only if you want the logo or ongoing work. Cost is 19 Connects.

> You mentioned optimizing Claygents and credit spend. The fastest win I usually find is Claygent or AI columns doing classification ("is this a fit?", "which industry bucket?"). Those can move to a decision model like Jev for a fraction of the cost, and Claygent then only runs on rows that pass. I'd start by auditing one table and showing you the credit cost before and after.
>
> Clay: end-to-end builds, Automated Outbound certified, pipelines at 10K+ leads/month, tables joined into HubSpot and Salesforce. Not a certified partner, but happy to share a walkthrough of a live build.

### c) Skip: "Inc. 5000 Executive Contact Build"
$300 for 15–25K contacts on your own Clay license loses money. The client also has several 1-star reviews from freelancers.

## 3. Reusable proposal opener
> Most Clay tables spend their credits on decisions, not writing: is this a fit, which persona, is this reply a "not now" or a "never." I move those onto Jev, a decision model that returns a typed answer plus a calibrated confidence for about $1 per 100K rows, and keep LLM columns for the writing. You see the side-by-side on your own rows before anything switches.

**Searches to run daily** (I can do this for you with `find_jobs`): "Clay scoring", "lead qualification Clay", "Claygent credits", "ICP scoring", "reply classification", "lead routing".
