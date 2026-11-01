# Milestone 4: Second Signal, Combining Rule, Calibration

## The combining rule, written before the code

Written before `scoring.py::combine_signals` was touched. Numbers can move
after calibration, but if they do, the change gets recorded at the bottom
instead of quietly replacing this.

1. **Base: an equal-weight average.** `0.5 × model_score + 0.5 × style_score`.
   Neither signal gets more weight. The model signal is biased against plain
   writers, and the style signal is cheap to game, so I don't trust either one
   more than the other.
2. **Disagreement means unsure.** If the two signals are more than **0.40**
   apart, the result is clamped into the unsure band (above 0.20 and below
   0.80, criterion 3). Two methods pointing opposite ways is uncertainty, and
   the service shouldn't make a confident claim on the strength of one of them.
3. **Too little text means unsure.** Under **3 sentences or 50 words**, the style
   measures have almost nothing to work with, so the result is clamped into
   the unsure band too.

What this means in practice: a high-confidence AI label (≥ 0.80) needs the
**average** at 0.80 or more **and** the two signals within 0.40 of each other.
So the style signal has to be at least 0.60 even if the model signal is 1.0.
A high model score alone, which is what the Milestone 1 garden paragraph got,
can't produce an accusation.

---

## Calibration (`python calibrate.py`)

Inputs are in `calibration/texts.py`, with where each came from. The AI texts
are written by Claude; the human ones are real r/csmajors comments from
TakeMeter.

| Set | n | model (avg) | style (avg) | combined (avg) | ≥ 0.80 (AI label) | ≤ 0.20 (human label) |
|---|---|---|---|---|---|---|
| clearly AI | 6 | 0.819 | 0.871 | 0.845 | 5 | 0 |
| lightly edited AI | 2 | 0.436 | 0.542 | 0.489 | 0 | 0 |
| clearly human | 14 | 0.357 | 0.321 | 0.342 | 0 | 1 |
| plain human | 10 | 0.331 | 0.399 | 0.365 | 0 | 0 |

**Raw measure ranges, which set the style ramps:**

| Measure | AI texts | Human texts | Direction |
|---|---|---|---|
| sentence-length spread (CV) | 0.14 – 0.36 | 0.22 – 0.94 | low = AI, as expected |
| type-token ratio (MATTR, 50-word window) | 0.88 – 0.94 | 0.76 – 0.95 | **high = AI, the opposite of the brief's guess** |
| varied punctuation per 100 words | 0.00 – 1.06 | 0.00 – 11.8 | low = AI, as expected |

**What I found:**

- **Vocabulary variety runs backwards.** Assistant-style prose almost never
  repeats a word inside 50 words. People repeat "I", "the", "it" and whatever
  they're talking about. So the ramp treats *high* variety as AI-ish.
- **That reversal protects plain writers.** The Milestone 1 garden paragraph
  still gets `model_score` 0.79, but its repetition gives a style score of 0.57
  and a combined 0.68, which is unsure (below 0.80), not an accusation.
- **Light editing defeats both signals.** Contractions, one short sentence, a
  dash and a typo dropped two AI texts from about 0.85 to about 0.49. That's a
  known blind spot and will be in Unit 8's attack set.
- **Plain human writing was *not* the worst case on this data.** Real plain
  Reddit comments scored a lower model signal (0.33 average) than I predicted.
  Slang, typos and missing punctuation surprise GPT-2. The risky case is
  plain writing that is also *tidy*, like the garden paragraph.
- **Caveat:** the ramps were set from these same texts, so these numbers flatter
  the signal. Criteria 1 and 2 need fresh samples, not this set.

## A case where the signals split

**Human comment #1** ("This is cope. People from prestigious schools…", a real
r/csmajors comment): `model_score` **0.515**, `style_score` **0.105**. The model
is at a coin flip; style is confident it's human (uneven sentences, lots of
repetition, quotes).

What the rule does: the average is 0.31, which is already in the unsure band.
The gap (0.41) is over 0.40, so rule 2 also fires, and it would keep the result
unsure even if the weights changed to favour style. Result: **unsure, 0.31**.
Style alone, at 0.105, would have called it human. The average stops either
signal deciding alone.

## Revisions after calibration

- **Rule 2 is implied by the thresholds as they stand.** With equal weights and
  criterion 3's 0.20 / 0.80, an average ≥ 0.80 already forces both signals ≥
  0.60, which is a gap of at most 0.40. So rule 2 can't change a label by itself
  right now. I kept it as an explicit guard, because it starts to matter the
  moment the weights or thresholds move. Rule 3 (short text) does change
  outcomes: the `detector.py` sample (47 words) would average 0.69 and is held
  at the top of the unsure band instead.
- **Style needs 50 words.** `stylometry.MIN_WORDS = 50` and `MIN_SENTENCES = 3`
  match rule 3, so a short submission gets `style_score` 0.5 (no opinion).
