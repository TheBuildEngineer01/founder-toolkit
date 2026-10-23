#!/usr/bin/env python3
"""
Inquiry Triage Starter
----------------------
Sorts incoming customer messages (WhatsApp, Instagram DMs, website chat, email)
into ORDER / QUESTION / COMPLAINT / OTHER, pulls out a few useful details,
and drafts a polite first reply from editable templates.

Rule-based on purpose: no API keys, no cost, easy to understand.
Swap `classify()` for an AI model later if you need smarter sorting.

Usage:
    python triage.py "Hi, is this still available? How much?"
    python triage.py --file sample_messages.txt
    python triage.py --file sample_messages.txt --json
"""
import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_rules(path=HERE / "rules.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _contains(text, words):
    return [w for w in words if re.search(r"\b" + re.escape(w) + r"\b", text)]


def classify(text, rules):
    """Return (category, matched_keywords). Highest keyword score wins;
    complaints win ties because they are the most urgent."""
    t = text.lower()
    scores = {}
    for cat in ("complaint", "order", "question"):
        hits = _contains(t, rules["keywords"][cat])
        if hits:
            scores[cat] = hits
    if not scores:
        return "other", []
    priority = {"complaint": 3, "order": 2, "question": 1}
    best = max(scores, key=lambda c: (len(scores[c]), priority[c]))
    return best, scores[best]


def extract_details(text, rules):
    t = text.lower()
    details = {}
    qty = re.search(r"\b(\d{1,3})\s*(pcs|pieces|units|items|x)\b", t) or \
        re.search(r"\b(?:need|want|order|buy)\s+(\d{1,3})\b", t)
    if qty:
        details["quantity"] = int(qty.group(1))
    for city in rules["cities"]:
        if re.search(r"\b" + re.escape(city.lower()) + r"\b", t):
            details["city"] = city
            break
    if _contains(t, rules["keywords"]["urgent"]):
        details["urgent"] = True
    return details


def draft_reply(category, details, rules):
    reply = rules["replies"][category]
    missing = [f for f in rules["ask_for"].get(category, []) if f not in details]
    if missing:
        reply += " " + rules["follow_up_question"].format(fields=" and ".join(missing))
    return reply


def triage(text, rules):
    category, hits = classify(text, rules)
    details = extract_details(text, rules)
    return {
        "message": text,
        "category": category.upper(),
        "matched": hits,
        "details": details,
        "hot_lead": category == "order" or bool(details.get("urgent")),
        "suggested_reply": draft_reply(category, details, rules),
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description="Sort customer messages and draft a first reply.")
    ap.add_argument("message", nargs="?", help="a single message to triage")
    ap.add_argument("--file", help="text file with one message per line")
    ap.add_argument("--rules", default=str(HERE / "rules.json"), help="path to rules.json")
    ap.add_argument("--json", action="store_true", help="print JSON instead of a readable summary")
    args = ap.parse_args(argv)

    rules = load_rules(args.rules)
    if args.file:
        lines = Path(args.file).read_text(encoding="utf-8").splitlines()
        messages = [ln.strip() for ln in lines if ln.strip() and not ln.startswith("#")]
    elif args.message:
        messages = [args.message]
    else:
        ap.print_help()
        return 1

    results = [triage(m, rules) for m in messages]
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0
    for r in results:
        flag = "  🔥 HOT LEAD" if r["hot_lead"] else ""
        print(f"[{r['category']}]{flag}  {r['message']}")
        if r["details"]:
            print(f"   details: {r['details']}")
        print(f"   reply:   {r['suggested_reply']}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
