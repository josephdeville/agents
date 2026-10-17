#!/usr/bin/env python3
"""Score a CSV with Jev outside Clay (for TAM sprints and buyer maps).

    TYPESAFE_API_KEY=... python3 jev_batch.py in.csv out.csv clay-templates/persona_icp.json
    python3 jev_batch.py in.csv out.csv clay-templates/persona_icp.json --dry-run

The template's "state" uses {{Column Name}} placeholders that match CSV headers.
Placeholders without a matching header (for example [BRACKETS]) are left as-is,
so fill those in first. Standard library only.
"""
import argparse, csv, json, os, re, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

URL = "https://api.typesafe.ai/v1/systemone"
RETRY = {429, 529, 500, 502, 503}


def render(state, row):
    return re.sub(r"\{\{\s*(.+?)\s*\}\}", lambda m: str(row.get(m.group(1), "")).strip(), state)


def call(body, key, tries=5):
    data = json.dumps(body).encode()
    for i in range(tries):
        req = urllib.request.Request(URL, data=data, headers={
            "Authorization": f"Bearer {key}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in RETRY and i < tries - 1:
                time.sleep(2 ** i)
                continue
            return {"error": f"HTTP {e.code}: {e.read()[:200].decode(errors='replace')}"}
        except urllib.error.URLError as e:
            if i < tries - 1:
                time.sleep(2 ** i)
                continue
            return {"error": str(e)}


def flatten(resp):
    if "error" in resp:
        return {"jev_error": resp["error"]}
    out = {}
    for q, a in resp.get("answers", {}).items():
        for k, v in a.items():
            if k != "probabilities":
                out[f"{q}_{k}"] = v
        conf = a.get("confidence")
        if isinstance(conf, (int, float)):
            out[f"{q}_lane"] = "auto" if conf >= 0.9 else "review" if conf >= 0.7 else "hold"
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("inp"); p.add_argument("out"); p.add_argument("template")
    p.add_argument("--workers", type=int, default=8)
    p.add_argument("--limit", type=int, default=0, help="only first N rows (start with 50)")
    p.add_argument("--dry-run", action="store_true", help="print request bodies, no API calls")
    a = p.parse_args()

    tpl = json.load(open(a.template))
    rows = list(csv.DictReader(open(a.inp, newline="", encoding="utf-8-sig")))
    if a.limit:
        rows = rows[:a.limit]
    bodies = [{**tpl, "state": render(tpl["state"], r)} for r in rows]

    if a.dry_run:
        for b in bodies[:3]:
            print(json.dumps(b, indent=2))
        print(f"... {len(bodies)} rows, ~{sum(len(b['state']) for b in bodies)//4:,} state tokens", file=sys.stderr)
        return

    key = os.environ.get("TYPESAFE_API_KEY") or sys.exit("set TYPESAFE_API_KEY")
    with ThreadPoolExecutor(a.workers) as ex:
        results = list(ex.map(lambda b: flatten(call(b, key)), bodies))

    cols = list(rows[0].keys()) if rows else []
    extra = sorted({k for r in results for k in r})
    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols + extra)
        w.writeheader()
        for r, res in zip(rows, results):
            w.writerow({**r, **res})
    errs = sum("jev_error" in r for r in results)
    print(f"wrote {len(rows)} rows to {a.out} ({errs} errors)", file=sys.stderr)


if __name__ == "__main__":
    main()
