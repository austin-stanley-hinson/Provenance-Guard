#!/usr/bin/env python3
"""
Criterion 4: ten appeals, three trials.  (Unit 8, Milestone 3)

    PORT=5050 python run_appeal_eval.py --label before

run_eval.py only sends /submit, and an appeal needs the content_id a
submission returned. So each trial here:

  1. submits 10 texts (one creator_id each, so the rate limit isn't involved)
  2. appeals every content_id that came back, with its own reasoning
  3. checks, for each appeal:
       - the response is 200 with status "under_review" and a message
       - logs/audit.jsonl (via GET /log) has an appeal entry with that
         content_id and exactly that reasoning
       - the latest log entry for that content_id has status "under_review"

A trial's score is how many of the 10 pass all three checks. Target: 10 of 10
in every trial.
"""

import argparse
import datetime as dt
import json

import requests

import config
from scenarios import AI_FRESH

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"


def run_trial(url, trial):
    sent = []
    for i, text in enumerate(AI_FRESH, 1):
        r = requests.post(f"{url}/submit", timeout=90,
                          json={"text": text, "creator_id": f"eval_appeal_t{trial}_{i}"})
        sent.append((i, r.status_code, r.json().get("content_id")))

    results = []
    for i, status, cid in sent:
        reasoning = f"Trial {trial}, piece {i}: I wrote this myself and would like a review."
        r = requests.post(f"{url}/appeal", timeout=30,
                          json={"content_id": cid, "reasoning": reasoning})
        body = r.json()
        results.append({"piece": i, "submit_status": status, "content_id": cid,
                        "reasoning": reasoning, "appeal_status": r.status_code,
                        "response": body})

    entries = requests.get(f"{url}/log", timeout=30).json()["entries"]
    for res in results:
        mine = [e for e in entries if e.get("content_id") == res["content_id"]]
        logged = any(e.get("event") == "appeal" and e.get("reasoning") == res["reasoning"]
                     for e in mine)
        latest = mine[-1].get("status") if mine else None
        ok_response = (res["appeal_status"] == 200
                       and res["response"].get("status") == "under_review"
                       and bool(res["response"].get("message")))
        res.update(logged_with_reasoning=logged, latest_status=latest,
                   passed=ok_response and logged and latest == "under_review")
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    args = parser.parse_args()

    trials = []
    for t in range(1, args.trials + 1):
        results = run_trial(args.url, t)
        passed = sum(r["passed"] for r in results)
        print(f"  trial {t}: {passed}/{len(results)} appeals recorded, under_review, confirmed")
        trials.append(results)

    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"appeal_run_{stamp}{label}.md"
    lines = [f"# Appeal run (criterion 4){f' — {args.label}' if args.label else ''}", "",
             "- Produced by: `run_appeal_eval.py::main`",
             "- Service: `app.py::submit`, `app.py::appeal`, `GET /log`", "",
             "| Trial | Passed |", "|---|---|"]
    lines += [f"| {i} | {sum(r['passed'] for r in rs)}/{len(rs)} |" for i, rs in enumerate(trials, 1)]
    lines += ["", "## What actually came back", ""]
    for i, rs in enumerate(trials, 1):
        lines += [f"**Trial {i}**", "", "```json", json.dumps(rs, indent=2), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
