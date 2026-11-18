# Capstone: criteria topics (menu, not criteria)

Claude drafted this as a menu. **The five criteria themselves go in
`criteria.md` under `## Capstone criteria`, written by me, with my numbers,
committed before any capstone run.** At least 3 of the 5 must be about the
extension (logging, timing, cost, run path), not about detection quality.

Pick five. Each blank is a number or condition I choose and defend in one sentence.

## About the extension (need at least 3)

1. **Log completeness:** of ___ requests (mix of good, bad, and too-long),
   ___% write a log line containing every required field:
   `timestamp, route, input (text_chars / words), output (label or reason), duration_ms`.
   Why this number: a request missing from the log is invisible later.

2. **Warm latency:** after the model is loaded, a ~150-word `/submit` takes
   ≤ ___ ms (median of ___ requests), measured from `duration_ms` in the log.
   Decide and say: *warm* only, not the first request.

3. **Cold start:** the first `/submit` after startup takes ≤ ___ s.
   (The model lazy-loads on the first request, so expect this one to miss before the fix.)

4. **Cost per run:** one `/submit` costs ≤ ___ seconds of CPU / ___ ms wall time,
   measured from the log over ___ requests. There's no API spend, so compute time is the cost.

5. **Run path reproducible:** following `RUNNING.md` exactly from a fresh
   `git clone`, the service answers `/health` within ___ minutes with zero
   undocumented steps. Count the extra steps needed; the target is ___.

6. **Rejections are timed too:** 400/413/422/429 responses are logged with
   `duration_ms` and come back in ≤ ___ ms (they should never touch the model).

7. **Stage breakdown:** each decision logs `model_ms` and `style_ms`, and
   `model_ms + style_ms` accounts for ≥ ___% of `duration_ms`.

## About the system as it already worked (at most 2)

8. Under gunicorn, the same 10 eval texts get the same labels as under `python app.py` (___ / 10 match).
9. Rate limiting still returns 429 on request ___ in a minute under gunicorn with 1 worker.

## Likely "one improvement" candidates (pick after the before-run)

- Load the model at startup instead of on the first request (fixes cold start).
- Raise the gunicorn `--timeout` if the first request gets killed.
- Cap the tokens scored per request if warm latency misses.
