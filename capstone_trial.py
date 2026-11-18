#!/usr/bin/env python3
"""
Capstone: one trial = fresh service start + the scripted batch from criteria.md.

    python capstone_trial.py before 1      # label, trial number

Starts the service with the exact RUNNING.md command, sends:
    1 first /submit (cold), 10 warm /submits, 8 bad requests
    (2 invalid JSON, 2 missing field, 2 too long, 2 over the rate limit),
then reads the NEW lines of logs/audit.jsonl, scores the five capstone
criteria, writes results/capstone/<label>_trial<N>.json, and stops the server.
"""

import json
import statistics
import subprocess
import sys
import time
from pathlib import Path

import requests

import config

PORT = 5050
BASE = f"http://127.0.0.1:{PORT}"
CMD = [".venv/bin/gunicorn", "app:app", "--bind", f"127.0.0.1:{PORT}",
       "--workers", "1", "--timeout", "120"]
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results" / "capstone"

# ~150 words, plain human-style prose. Same text every request, every trial.
TEXT = (
    "I started keeping a notebook by the back door last spring, mostly to track "
    "when the tomatoes went in and how often I actually watered them. It turned "
    "into something else. Some days I wrote about the weather, some days about the "
    "neighbor's dog that kept digging under the fence, and once, a whole page about "
    "my grandmother's kitchen and the smell of burnt sugar. I don't think anyone "
    "else would care about most of it. But reading it back in October, I could see "
    "the whole season again: the week it rained every afternoon, the morning I found "
    "the first ripe one split open on the vine, the evening my brother came over and "
    "we ate standing up in the yard because the chairs were still wet. The notebook "
    "is half mud now. I'm keeping it anyway, and I already bought another one for "
    "next year, even though I swore I'd plant less."
)


def post(payload=None, raw=None):
    if raw is not None:
        return requests.post(f"{BASE}/submit", data=raw,
                             headers={"Content-Type": "application/json"}, timeout=180)
    return requests.post(f"{BASE}/submit", json=payload, timeout=180)


def wait_for_health(deadline_s=60):
    end = time.time() + deadline_s
    while time.time() < end:
        try:
            if requests.get(f"{BASE}/health", timeout=2).ok:
                return
        except requests.RequestException:
            pass
        time.sleep(0.5)
    raise RuntimeError("service never answered /health")


def run_batch(tag):
    codes = {}
    codes["cold"] = post({"creator_id": f"{tag}-cold", "text": TEXT}).status_code
    codes["warm"] = [post({"creator_id": f"{tag}-warm{i}", "text": TEXT}).status_code
                     for i in range(10)]
    bad = []
    bad += [post(raw="not json {").status_code for _ in range(2)]
    bad += [post({"creator_id": f"{tag}-missing{i}"}).status_code for i in range(2)]
    bad += [post({"creator_id": f"{tag}-long{i}", "text": "x " * (config.MAX_TEXT_CHARS // 2 + 1)}).status_code
            for i in range(2)]
    flood = [post({"creator_id": f"{tag}-flood", "text": TEXT}).status_code
             for _ in range(config.RATE_LIMIT_PER_MINUTE + 2)]
    bad += flood[-2:]
    codes["bad"] = bad
    codes["flood_all"] = flood
    return codes


def score(entries, tag):
    def mine(e, prefix):
        return str(e.get("creator_id", "")).startswith(f"{tag}-{prefix}")

    cold = [e for e in entries if mine(e, "cold") and e.get("status") == "decided"]
    warm = [e for e in entries if mine(e, "warm") and e.get("status") == "decided"]
    rejected = [e for e in entries if e.get("event") == "rejected"
                and (e.get("creator_id") == "unknown" or mine(e, "missing")
                     or mine(e, "long") or mine(e, "flood"))]

    warm_ms = [e["duration_ms"] for e in warm]
    warm_cpu = [e["cpu_ms"] for e in warm]
    shares = [(e["model_ms"] + e["style_ms"]) / e["duration_ms"] for e in warm]
    rej_ok = [e for e in rejected if "duration_ms" in e]

    c = {
        "1_warm_latency": {"median_ms": statistics.median(warm_ms), "target": "<= 500",
                           "met": statistics.median(warm_ms) <= 500, "n": len(warm_ms)},
        "2_cold_start": {"first_ms": cold[0]["duration_ms"] if cold else None,
                         "target": "<= 10000",
                         "met": bool(cold) and cold[0]["duration_ms"] <= 10_000},
        "3_cost_cpu": {"median_cpu_ms": statistics.median(warm_cpu), "target": "<= 1000",
                       "met": statistics.median(warm_cpu) <= 1000},
        "4_rejections": {"logged_with_duration": f"{len(rej_ok)}/8",
                         "max_ms": max((e["duration_ms"] for e in rej_ok), default=None),
                         "target": "8/8 logged, each <= 50",
                         "met": len(rej_ok) == 8 and all(e["duration_ms"] <= 50 for e in rej_ok)},
        "5_time_accounted": {"min_share_pct": round(min(shares) * 100, 1), "target": ">= 90",
                             "met": min(shares) >= 0.90},
    }
    return c


def main():
    label, n = sys.argv[1], int(sys.argv[2])
    tag = f"cap-{label}-t{n}"
    start_line = len(config.AUDIT_LOG.read_text().splitlines()) if config.AUDIT_LOG.exists() else 0

    server = subprocess.Popen(CMD, cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        wait_for_health()
        codes = run_batch(tag)
    finally:
        server.terminate()
        server.wait(timeout=30)

    new = [json.loads(l) for l in config.AUDIT_LOG.read_text().splitlines()[start_line:] if l.strip()]
    criteria = score(new, tag)
    OUT.mkdir(parents=True, exist_ok=True)
    out = {"label": label, "trial": n, "tag": tag, "http_codes": codes,
           "criteria": criteria, "log_entries": new}
    (OUT / f"{label}_trial{n}.json").write_text(json.dumps(out, indent=2))

    print(f"{label} trial {n}  codes: cold={codes['cold']} warm={set(codes['warm'])} bad={codes['bad']}")
    for k, v in criteria.items():
        print(f"  {'MET ' if v['met'] else 'MISS'}  {k}: {v}")


if __name__ == "__main__":
    main()
