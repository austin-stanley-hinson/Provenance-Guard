#!/usr/bin/env python3
"""
Score every calibration text with both signals, in one process.

    python calibrate.py            # summary per set + every row
    python calibrate.py --raw      # also print the three raw style measures

No service needed. This calls the same functions /submit calls.
"""

import statistics
import sys

import detector
import scoring
import stylometry
from calibration.texts import SETS

RAW = "--raw" in sys.argv


def main():
    rows = []
    for name, texts in SETS.items():
        for i, text in enumerate(texts, 1):
            m = detector.model_signal(text)
            s = stylometry.style_signal(text)
            c = scoring.combine_signals(m, s, text=text)
            rows.append((name, i, len(stylometry.words(text)), m, s, c,
                         stylometry.sentence_length_spread(text),
                         stylometry.type_token_ratio(text),
                         stylometry.punctuation_density(text),
                         text[:50].replace("\n", " ")))

    head = f"{'set':12} {'#':>2} {'words':>5} {'model':>6} {'style':>6} {'comb':>6}"
    if RAW:
        head += f" {'spread':>6} {'mattr':>6} {'punct':>6}"
    print(head + "  start")
    for r in rows:
        line = f"{r[0]:12} {r[1]:>2} {r[2]:>5} {r[3]:6.3f} {r[4]:6.3f} {r[5]:6.3f}"
        if RAW:
            line += f" {r[6]:6.3f} {r[7]:6.3f} {r[8]:6.2f}"
        print(line + f"  {r[9]}")

    print(f"\n{'set':12} {'n':>3} {'model':>6} {'style':>6} {'comb':>6}  ≥0.80  ≤0.20")
    for name in SETS:
        rs = [r for r in rows if r[0] == name]
        mean = lambda k: statistics.mean(r[k] for r in rs)  # noqa: E731
        hi = sum(r[5] >= 0.80 for r in rs)
        lo = sum(r[5] <= 0.20 for r in rs)
        print(f"{name:12} {len(rs):>3} {mean(3):6.3f} {mean(4):6.3f} {mean(5):6.3f}  {hi:>5}  {lo:>5}")


if __name__ == "__main__":
    main()
