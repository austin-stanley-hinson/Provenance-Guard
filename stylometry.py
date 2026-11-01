"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures ───────────────────────────────────────────────────────

# Below this, the measures have too little to go on. style_signal() reports
# "no opinion" (0.5) and scoring.combine_signals() keeps the result unsure.
MIN_SENTENCES = 3
MIN_WORDS = 50

# Moving-average window for the type-token ratio. See type_token_ratio().
TTR_WINDOW = 50

# The punctuation that varies between writers. Full stops and commas are left
# out on purpose: everyone uses them, so they say little about who's writing.
VARIED_PUNCTUATION = set(";:()[]!?'\"“”‘’…—–-")


def _sentence_lengths(text: str) -> list[int]:
    """
    Words per sentence. Splits on line breaks as well as . ! ?, because
    informal writing often ends a thought with a new line and no full stop.
    """
    lengths = []
    for line in text.splitlines():
        for sentence in sentences(line):
            n = len(words(sentence))
            if n:
                lengths.append(n)
    return lengths


def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies: the coefficient of variation
    (standard deviation ÷ mean) of words per sentence.

    Scale: 0 upward, usually 0.2–1.0. **Higher means more human** (lumpier).
    Fewer than two sentences returns 0.0. That is NOT "very AI-like", it means
    no reading, and style_signal() ignores it below MIN_SENTENCES.
    """
    lengths = _sentence_lengths(text)
    if len(lengths) < 2:
        return 0.0
    return round(statistics.stdev(lengths) / statistics.mean(lengths), 4)


def type_token_ratio(text: str) -> float:
    """
    Vocabulary variety: unique words over total words, averaged over a moving
    50-word window (MATTR).

    Scale: 0–1. **Higher means more varied vocabulary.**

    Plain TTR falls as text gets longer, so a 60-word post and a 600-word essay
    aren't comparable on it. Averaging over fixed-size windows removes most of
    that. Under 50 words it falls back to plain TTR.
    """
    w = words(text)
    if not w:
        return 0.0
    if len(w) <= TTR_WINDOW:
        return round(len(set(w)) / len(w), 4)
    ratios = [
        len(set(w[i:i + TTR_WINDOW])) / TTR_WINDOW
        for i in range(len(w) - TTR_WINDOW + 1)
    ]
    return round(statistics.mean(ratios), 4)


def punctuation_density(text: str) -> float:
    """
    Varied punctuation per 100 words: semicolons, colons, brackets, dashes,
    quotes, apostrophes, ! ? and ellipses. Full stops and commas don't count.

    Scale: 0 upward, usually 0–15. **Higher means more human**, see the
    calibration notes for why that direction and whether it held up.
    """
    w = words(text)
    if not w:
        return 0.0
    marks = sum(1 for ch in text if ch in VARIED_PUNCTUATION)
    return round(100 * marks / len(w), 4)


# ── Combining them ───────────────────────────────────────────────────────────

# Each measure is mapped onto 0–1 "AI-ness" with a straight ramp between two
# anchor values, clipped at the ends. The anchors come from the calibration run
# in notes/milestone4.md (6 AI texts, 25 real r/csmajors comments):
#
#   measure   AI texts       human texts    ramp: AI end -> human end
#   spread    0.14 – 0.36    0.22 – 0.94    0.20 -> 0.60   (low  = AI)
#   mattr     0.88 – 0.94    0.76 – 0.95    0.92 -> 0.80   (high = AI)
#   punct     0.00 – 1.06    0.00 – 11.8    0.50 -> 6.00   (low  = AI)
#
# ⚠️ mattr runs the OPPOSITE way to the brief's guess. Assistant-style prose
# rarely repeats a word inside 50 words, while people repeat "I", "the", "it"
# and the thing they're talking about. So varied vocabulary scores AI-ish here.
RAMPS = {
    "spread": (0.20, 0.60),
    "mattr": (0.92, 0.80),
    "punct": (0.50, 6.00),
}


def _ramp(value: float, ai_end: float, human_end: float) -> float:
    """1.0 at ai_end, 0.0 at human_end, straight line between, clipped."""
    t = (value - human_end) / (ai_end - human_end)
    return min(max(t, 0.0), 1.0)


def style_parts(text: str) -> dict[str, float]:
    """The three measures, each already turned into 0–1 AI-ness."""
    return {
        "spread": _ramp(sentence_length_spread(text), *RAMPS["spread"]),
        "mattr": _ramp(type_token_ratio(text), *RAMPS["mattr"]),
        "punct": _ramp(punctuation_density(text), *RAMPS["punct"]),
    }


def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    1. Each measure becomes 0–1 AI-ness with its ramp (see RAMPS above), which
       fixes both direction and scale: low spread, high vocabulary variety
       and little varied punctuation all push toward 1.
    2. The three are averaged with equal weight.

    Under MIN_SENTENCES sentences or MIN_WORDS words, it returns 0.5: no
    opinion. scoring.combine_signals() also keeps short text unsure, so a
    one-sentence submission can't be labelled either way by style alone.
    """
    if len(_sentence_lengths(text)) < MIN_SENTENCES or len(words(text)) < MIN_WORDS:
        return 0.5
    parts = style_parts(text)
    return round(sum(parts.values()) / len(parts), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    