# Offers

Founding prices apply to the first 3 clients per offer, in exchange for a testimonial and permission to use the numbers. After that, raise to the standard price.

---

## A. Clay Cost-Cut Audit (lead offer)
**One-liner:** "I move the judgment calls in your Clay tables off expensive AI columns onto a model that costs about $1 per 100K rows, then show you the before-and-after."

**Who buys:** teams and agencies spending $500+/month on Clay credits or OpenAI keys for classification, scoring, and routing.

**Scope**
1. Inventory every AI, Claygent, and formula column. Tag each one: *writes*, *researches*, or *decides*.
2. Rebuild the "decides" columns as Jev HTTP columns (choice, score, or yes/no), with an `unclear` option on each.
3. Run old and new side by side on 200 rows and report agreement, cost per row, and speed.
4. Add confidence lanes (≥0.90 auto, 0.70–0.90 review, <0.70 hold) and gate the expensive downstream columns on them.
5. Loom walkthrough plus a written decision log.

**Price:** $750 founding / $1,500–3,000 standard. Optional: 25% of first-year savings instead.
**Time:** 3–5 days.

---

## B. Whole-TAM Scoring Sprint
**One-liner:** "Stop guessing which slice of your market to work. I score every company or person in it and hand back a ranked list with confidence."

**Scope**
1. Use an LLM to draft a detailed fit description from the client's call notes and closed-won accounts.
2. Build evidence packets: a short, labeled state for each record (title, headline, about, current roles, company facts).
3. Score with Jev using several questions per call (fit, persona, timing signal).
4. Deliver a ranked CSV or Clay table with lanes and the top 200 hand-checked.

**Price:** $2,500 founding / $5,000–7,500 standard. Data costs passed through at cost.
**Time:** 1–2 weeks.

---

## C. Enterprise Account Buyer Map
**One-liner:** "Give me one enterprise account. I'll score every employee for fit with your product and find the buyers your title search missed."

**Who buys:** AEs and SDR leads selling into 10K+ employee companies.

**Deliverable:** every employee scored 5→1 (5 = buyer or owning dept, 4 = daily user, 3 = adjacent, 2 = other, 1 = exclude), the titles a search would miss, and a call list with reasons.

**Price:** $400/account founding, $750 standard. $3K/month for 10 accounts.
**Time:** 48 hours per account.

---

## D. Managed Signal Triage (retainer)
**One-liner:** "Every inbound lead, reply, and job post gets classified and routed within minutes, with nothing written by a model that can hallucinate."

**Runs on:**
- inbound form fills (ICP fit and routing)
- cold-email replies (interested / not now / never / OOO / wrong person / unsubscribe)
- job posts (hiring signal for the client's product, yes/no)

Results push to HubSpot or Salesforce, with a weekly accuracy check.

**Price:** $1,000–3,000/month depending on volume and number of sources. Setup fee $500.

---

## E. Jev for Clay template pack (digital product)
- 6 copy-paste HTTP column bodies (see `clay-templates/`)
- Lane formula, run conditions, error handling (429/529/422)
- Criteria-writing guide: no overlap, always an `unclear` option, short state
- Sell on Gumroad or Lemon Squeezy at **$49**. A $149 tier adds a 30-minute setup call.

---

## Objection answers
- **"Is it accurate?"** "I'll run it next to your current column on 200 rows and show you the agreement rate before you switch anything."
- **"It's early access."** "Every build keeps your current column as a fallback behind a switch."
- **"Why not just use GPT-mini?"** "You still parse free text, and the confidence it reports isn't calibrated. Jev returns typed answers, and its confidence scores are trained to match how often it's right, so your routing lanes can trust them."
