#!/usr/bin/env python3
"""Run the same hiring-signal query through Perplexity so it can be compared with Exa.

    export PERPLEXITY_API_KEY=...        # your key, set in your own shell, never in chat
    python3 perplexity_brief.py                  # sonar-pro, 5 companies (cheap)
    python3 perplexity_brief.py --model sonar-deep-research   # only if sonar-pro looks weak

Prints the answer, the citations, and whatever usage/cost fields the API returns.
Standard library only. One request per run, no retries, so a failure never double-spends.
"""
import argparse, json, os, sys, urllib.request, urllib.error

QUERY = (
    "Find 5 US B2B software companies with 20-200 employees that have an OPEN sales development "
    "(SDR/BDR) or founding sales role posted in the last 14 days. For each: company name, website, "
    "what they sell in one sentence, the job post URL with its posted date, and who leads sales or the "
    "founder (name + title) if publicly stated. Exclude staffing firms, job boards, marketing agencies, "
    "and companies that sell sales or outbound software. Every fact needs a source URL. If a fact "
    "cannot be verified, write null rather than guessing. Return JSON: "
    '{"companies":[{"name","website","what_they_sell","employees","job_title","job_url",'
    '"job_posted_date","sales_lead","sources":[]}]}'
)

ap = argparse.ArgumentParser()
ap.add_argument("--model", default="sonar-pro")
ap.add_argument("--max-tokens", type=int, default=1500)
a = ap.parse_args()

key = os.environ.get("PERPLEXITY_API_KEY") or sys.exit("set PERPLEXITY_API_KEY in your shell first")
body = json.dumps({"model": a.model, "max_tokens": a.max_tokens,
                   "messages": [{"role": "user", "content": QUERY}]}).encode()
req = urllib.request.Request("https://api.perplexity.ai/chat/completions", data=body,
                             headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req, timeout=180) as r:
        d = json.load(r)
except urllib.error.HTTPError as e:
    sys.exit(f"HTTP {e.code}: {e.read()[:300].decode(errors='replace')}")

print(d["choices"][0]["message"]["content"])
print("\nCITATIONS:", *(d.get("citations") or d.get("search_results") or []), sep="\n  ")
print("\nUSAGE:", json.dumps(d.get("usage", {}), indent=2))
