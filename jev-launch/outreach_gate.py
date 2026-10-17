#!/usr/bin/env python3
"""Outreach gate logic: decide pass/fail from Jev answers and build the rewrite prompt.

No network calls. Feed it the "answers" object from the Jev response for
clay-templates/outreach_gate.json. Standard library only.

    python3 outreach_gate.py --selftest
"""
import json
import sys

MIN_CONF = 0.80
MAX_ROUNDS = 2

# check name -> (test on the answer, instruction for the rewrite)
FIXES = {
    "specific_reference": "Open with one specific fact about this person or company, taken word for word from the evidence. Do not open with a greeting or a compliment.",
    "claims_supported": "Remove or rewrite every claim about the recipient that is not stated in the evidence. Do not guess, round up, or infer.",
    "generic_risk": "Make it impossible to send this to another company: tie the offer to the specific situation in the evidence.",
    "relevance": "State in one sentence how their evidenced situation connects to the offer, and why it matters now.",
    "ask": "End with exactly one small ask, such as a one-line reply or a yes/no question. Remove all other asks and any request for a call.",
    "tone": "Plain and direct. Remove superlatives, buzzwords, urgency and apologies.",
}


def prob(a):
    """Yes-probability from a noul answer. Field names are unverified: accept a float or a dict."""
    if isinstance(a, (int, float)):
        return float(a)
    for k in ("probability", "p", "value", "yes"):
        if isinstance(a, dict) and isinstance(a.get(k), (int, float)):
            return float(a[k])
    raise ValueError(f"cannot read probability from {a!r}")


def conf(a):
    return float(a.get("confidence", 0)) if isinstance(a, dict) else 1.0


def evaluate(ans):
    """Return (passed, failed_checks). A low-confidence answer counts as a fail."""
    failed = []
    if prob(ans["specific_reference"]) < 0.5 or conf(ans["specific_reference"]) < MIN_CONF:
        failed.append("specific_reference")
    if prob(ans["claims_supported"]) < 0.5 or conf(ans["claims_supported"]) < MIN_CONF:
        failed.append("claims_supported")
    if prob(ans["generic_risk"]) >= 0.5 or conf(ans["generic_risk"]) < MIN_CONF:
        failed.append("generic_risk")
    if ans["relevance"].get("score", 0) < 3 or conf(ans["relevance"]) < MIN_CONF:
        failed.append("relevance")
    if ans["ask"].get("choice") != "single_low_friction" or conf(ans["ask"]) < MIN_CONF:
        failed.append("ask")
    if ans["tone"].get("choice") != "plain" or conf(ans["tone"]) < MIN_CONF:
        failed.append("tone")
    return (not failed), failed


def rewrite_prompt(draft, evidence, failed):
    fixes = "\n".join(f"- {FIXES[f]}" for f in failed)
    return (
        "Rewrite this cold email. Fix ONLY the problems listed. Keep everything that already works.\n\n"
        f"Evidence (the only facts you may use about the recipient):\n{evidence}\n\n"
        f"Draft:\n{draft}\n\n"
        f"Problems to fix:\n{fixes}\n\n"
        "Rules: use only facts from the evidence; invent no numbers, names or results; "
        "keep it under the same length; one ask; plain tone. "
        "Return only the new email, then on a new line 'USED:' followed by the evidence facts you relied on."
    )


def next_step(round_no, passed, failed):
    """round_no counts rewrites already done."""
    if passed:
        return "approve"
    if round_no >= MAX_ROUNDS:
        return "human_or_drop"
    return "rewrite"


def _selftest():
    good = {"specific_reference": {"probability": .95, "confidence": .9},
            "claims_supported": {"probability": .92, "confidence": .9},
            "generic_risk": {"probability": .1, "confidence": .9},
            "relevance": {"score": 3.4, "confidence": .85},
            "ask": {"choice": "single_low_friction", "confidence": .9},
            "tone": {"choice": "plain", "confidence": .9}}
    ok, failed = evaluate(good)
    assert ok and not failed, failed
    bad = json.loads(json.dumps(good))
    bad["generic_risk"]["probability"] = .8
    bad["ask"]["choice"] = "multiple_asks"
    bad["tone"]["confidence"] = .5
    ok, failed = evaluate(bad)
    assert not ok and failed == ["generic_risk", "ask", "tone"], failed
    assert next_step(0, ok, failed) == "rewrite"
    assert next_step(2, ok, failed) == "human_or_drop"
    assert next_step(1, True, []) == "approve"
    p = rewrite_prompt("Hi, we help companies grow.", "- Hiring 2 SDRs (job post, 2026-09-30)", failed)
    assert "exactly one small ask" in p and "Hiring 2 SDRs" in p
    print("selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        _selftest()
    else:
        print(__doc__)
