# Finding clients (no Jev test runs)

Rule: **no Jev spend until a client is paying.** The first paid pilot is your case study. Offer it as "a pilot on your data, Jev cost on me." It's pennies, and the client provides the rows.

## A. Upwork: apply now (pulled Oct 2)
Connects balance: 186.

### 1. GTM engineer for a UK email agency (Clay + Lemlist + HubSpot + Asana)
- **Link:** https://www.upwork.com/jobs/~022102742506846095415
- **Terms:** hourly, $10–100/hr, 9 proposals, 1 hire so far, 19 Connects
- **Fit:** strong. This is your stack, and the AI-summary step is where Jev or an LLM fits.
- **Caveats:** the client has spent only $307 on Upwork, and they want a link to a Clay table. Use a sanitized one.
- **Bid:** $65/hr.

They'll only read proposals that answer all six questions:

> I've built this stack end to end. Most recently: three outbound campaigns in Instantly and HeyReach for a software modernization firm (Help4Access), including suppression and dedupe logic. Before that, Clay → HubSpot pipelines enriching 10,000+ leads/month, still running. HubSpot Revenue Ops certified, Clay Automated Outbound certified.
>
> **1. DNS records on a sending domain**
> - **MX:** where your inbound mail goes. I don't touch it, which is how your client email stays safe. Before any change I export the zone file and change one record at a time.
> - **SPF (TXT):** lists the servers allowed to send as you. One SPF record only: merge into it, never add a second. Stay under 10 DNS lookups.
> - **DKIM (TXT/CNAME):** the signing key that proves the mail wasn't altered. One per sending provider.
> - **DMARC (TXT at `_dmarc`):** tells receivers what to do when SPF or DKIM fails, and where to send reports. Start at `p=none` with reporting, then move to quarantine once the reports are clean.
> - **Tracking CNAME:** for a custom tracking domain (Q2).
> - **A/CNAME:** for the website. Untouched.
>
> **2. Custom tracking domain.** The built-in one is shared with every other sender on the platform, so you inherit their reputation, and their spam complaints land on your links. A custom subdomain keeps link reputation tied to you and aligned with your sending domain.
>
> **3. Reply rate drops from 4% to 0.5% in a week.** I check in this order:
> 1. Is mail actually sending? Mailbox disconnected, bounces, sequence paused.
> 2. Inbox placement: a seed test across Gmail and Outlook.
> 3. Authentication: did a DNS change break SPF or DKIM? Check DMARC reports.
> 4. Blocklists.
> 5. The list: new segment, verification skipped, data source changed.
> 6. The copy: new links, attachments, or wording that triggers filters.
> 7. Only then the market.
>
> **4. Daily volume.** About 30 cold sends a day, follow-ups included, from a single warmed mailbox on an aged business domain, ramping up from 10. That mailbox also carries client mail, so protecting it matters more than squeezing out 50/day. If you want more volume later, the answer is more mailboxes, not more per mailbox.
>
> **5. Clay table:** [LINK — add a sanitized table or a Loom walkthrough]
>
> **6. AI summary step.** One Zapier step that sends the week's HubSpot and Asana data to an LLM API with a fixed prompt and template, and writes the plain-English summary into the report. For the "last interaction" view: a HubSpot property updated by workflow, so it's one field rather than three tools. No platform, just a step.
>
> Handover: live walkthrough plus a written runbook. Happy to start with the DNS audit as milestone one.

### 2. Clay Specialist for Account Qualification (manufacturers/OEMs)
Proposal already drafted in `02-upwork.md` §2a. 20 Connects. They have 1 hire already, so it's a longer shot.

### 3. Patronus AI invite: RevOps expert reviewer, $50–150/task
Costs no Connects (it's an invitation). Fastest cash. Answer their three questions briefly.

### Skip
- Under $30/hr for expert work: the "GTM/RevOps Engineer" team ($20–30), HubSpot + Clay fintech ($8–20), Clay setup ($20 fixed).
- Clients rated under 3★ by freelancers (for example the ALEET posting, 1.59★).

## B. Outside Upwork: where better-paying clients are
Upwork's Clay market is underpriced. Direct outreach is where $1.5K+ audits come from.

1. **Clay agencies.** They have clients, credit bills, and margin pressure. Pitch the white-label offer (DM v2 in `03-outreach.md`).
2. **B2B SaaS companies (50–500 employees) hiring "GTM Engineer" or "RevOps" right now.** A job post is a budget signal. Offer the audit as faster and cheaper than a hire.
3. **People engaging with Jev posts.** The X demos, and comments on the Blueprint GTM and GTM Engineering newsletters. They're already interested and need a builder.
4. **Oct 7 SF event (Blueprint GTM, $150).** Agency owners in one room. Only worth it if you can be in SF.

**Building the list costs credits**, either Clay or Vibe Prospecting. I'll get a cost estimate before pulling anything, starting with 50 accounts.
