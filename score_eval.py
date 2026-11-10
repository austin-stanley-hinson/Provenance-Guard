#!/usr/bin/env python3
"""
Turn a run_eval.py report into per-trial numbers for criteria 1, 2, 3 and 5.

    python score_eval.py results/run_<stamp>_before.md

Reads the JSON blocks the report already contains, plus logs/audit.jsonl for
criterion 5's "no decision created" check. Prints one run-log row per criterion.
"""

import json
import re
import statistics
import sys

import audit


def trials_by_scenario(md):
    out = {}
    for block in re.split(r"^### ", md, flags=re.M)[1:]:
        name = block.splitlines()[0].strip()
        out[name] = [json.loads(j) for j in re.findall(r"```json\n(.*?)\n```", block, re.S)]
    return out


def main(path):
    t = trials_by_scenario(open(path, encoding="utf-8").read())
    n = len(t["c1 human writing, unseen"])
    rows = []

    c1 = [sum(r.get("guess") == "ai" for r in tr) for tr in t["c1 human writing, unseen"]]
    rows.append(("1. Human writing labelled AI", "≤ 1 of 20",
                 [f"{x}/20" for x in c1], all(x <= 1 for x in c1)))

    gaps = []
    for h, a in zip(t["c2 human half"], t["c2 AI half"]):
        mh = statistics.mean(r["combined_score"] for r in h)
        ma = statistics.mean(r["combined_score"] for r in a)
        gaps.append((ma - mh, ma, mh))
    rows.append(("2. AI mean − human mean (combined)", "≥ 0.25",
                 [f"{g:.3f} (AI {ma:.3f}, human {mh:.3f})" for g, ma, mh in gaps],
                 all(g >= 0.25 for g, _, _ in gaps)))

    c3 = [sorted({r.get("guess") for r in tr}) for tr in t["c3 label coverage"]]
    rows.append(("3. All three labels reached", "3 of 3",
                 [f"{len(set(g) & {'human', 'unsure', 'ai'})}/3 ({', '.join(g)})" for g in c3],
                 all({"human", "unsure", "ai"} <= set(g) for g in c3)))

    bad_ids = {"eval_bad_no_text", "eval_bad_empty", "eval_bad_space", "eval_bad_long"}
    decided = [e for e in audit.read_entries()
               if e.get("status") == "decided" and e.get("creator_id") in bad_ids]
    c5 = [sum(r.get("status") in (400, 413) and bool(r.get("error")) and bool(r.get("message"))
              for r in tr) for tr in t["c5 invalid input"]]
    rows.append(("5. Invalid input rejected, no decision", "5 of 5",
                 [f"{x}/5" for x in c5], all(x == 5 for x in c5) and not decided))

    print(f"{n} trials.  decisions logged for invalid-input creators: {len(decided)}\n")
    print("| Criterion | Target | " + " | ".join(f"Run {i}" for i in range(1, n + 1)) + " | Verdict |")
    print("|---|---|" + "---|" * n + "---|")
    for name, target, runs, met in rows:
        print(f"| {name} | {target} | " + " | ".join(runs) + f" | {'MET' if met else 'MISSED'} |")
    print("\n(criterion 4 comes from run_appeal_eval.py)")


if __name__ == "__main__":
    main(sys.argv[1])
