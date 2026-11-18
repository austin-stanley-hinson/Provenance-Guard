"""
Gunicorn settings for the capstone run path (see RUNNING.md).

The one improvement: load gpt2 when the worker starts, not on the first
request. Before this, the first writer of every session paid 2.6–4.2 s for
the model load. The load still happens; it just happens before anyone is
waiting, and it's logged as its own `startup` event so the cost stays visible.
"""

import time


def post_worker_init(worker):
    import audit
    import detector

    t0 = time.perf_counter()
    cpu0 = time.process_time()
    detector._load()
    audit._append({
        "timestamp": audit._now(),
        "event": "startup",
        "status": "model_loaded",
        "route": None,
        "duration_ms": round((time.perf_counter() - t0) * 1000, 1),
        "cpu_ms": round((time.process_time() - cpu0) * 1000, 1),
    })
