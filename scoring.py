"""
Turning two numbers into one, and one number into something a person can read.
← YOU BUILD THIS IN MILESTONES 4 AND 5

Two functions live here, and both are stubs.

`combine_signals` is where your false-positive decision from Milestone 1
actually gets made. Everything above it — the labels, the appeal path — is
downstream of a number this function produced.

`score_to_label` is where you stop writing for a machine and start writing for
a person. A score of 0.62 means nothing to a writer.

⚠️ Your README's **Signals and Scoring** section has to name the file and
function holding your combining rule. The grader checks your code against what
you claim, so that line should read `scoring.py::combine_signals`.
"""

import config


def combine_signals(model_score: float, style_score: float,
                    text: str | None = None) -> float:
    """
    Combine two 0–1 signals into one 0–1 score. 0.0 is confidently human, 1.0
    is confidently AI. Both inputs point the same way: higher means more AI.

    The rule (written down first, in notes/milestone4.md):

      1. **Equal-weight average.** WEIGHT_MODEL_SIGNAL × model +
         WEIGHT_STYLE_SIGNAL × style, 0.5 each. The model signal is biased
         against plain writers and the style signal is cheap to game, so
         neither is trusted over the other.
      2. **Disagreement means unsure.** If the signals are more than
         DISAGREEMENT_GAP apart, the result is clamped into the unsure band.
         Two methods pointing opposite ways is uncertainty, and one signal on
         its own never produces a confident label.
      3. **Too little text means unsure.** If `text` is given and is under
         MIN_SENTENCES sentences or MIN_WORDS words, the result is also
         clamped into the unsure band.

    Args:
        model_score: from `detector.model_signal`.
        style_score: from `stylometry.style_signal`.
        text: optional. Pass it so rule 3 can apply. /submit always does.
    """
    combined = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )

    disagree = abs(model_score - style_score) > config.DISAGREEMENT_GAP
    too_short = text is not None and _too_short(text)
    if disagree or too_short:
        combined = _clamp_unsure(combined)

    return round(min(max(combined, 0.0), 1.0), 4)


def _too_short(text: str) -> bool:
    import stylometry
    return (len(stylometry._sentence_lengths(text)) < stylometry.MIN_SENTENCES
            or len(stylometry.words(text)) < stylometry.MIN_WORDS)


def _clamp_unsure(score: float) -> float:
    """Pull a score just inside the unsure band, keeping which way it leaned."""
    low = config.HUMAN_THRESHOLD + 0.01
    high = config.AI_THRESHOLD - 0.01
    return min(max(score, low), high)


# The exact text a reader sees. Every one of them says how to ask for a review,
# not just the AI one: an appeal shouldn't feel like something you only get
# after being accused.
LABEL_HUMAN = (
    "This looks like it was written by a person. If you think we got that "
    "wrong, you can ask for a review."
)
LABEL_UNSURE = (
    "We can't tell whether this was written by a person or with help from AI. "
    "That happens a lot, especially with short or plainly written pieces, and "
    "it isn't an accusation. If you'd like a person to take a look, you can ask "
    "for a review."
)
LABEL_AI = (
    "This shows strong signs of being written with AI. Our check can be wrong. "
    "If you wrote this yourself, you can ask for a review and a person will "
    "look at it."
)


def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn a combined score into (guess, label_text).

        score <= HUMAN_THRESHOLD (0.20)  -> "human"
        score >= AI_THRESHOLD    (0.80)  -> "ai"
        anything in between              -> "unsure"

    Every score from 0 to 1 lands in exactly one band, with no gaps (criterion 3).
    """
    if score >= config.AI_THRESHOLD:
        return "ai", LABEL_AI
    if score <= config.HUMAN_THRESHOLD:
        return "human", LABEL_HUMAN
    return "unsure", LABEL_UNSURE


def label_ranges() -> list[tuple[str, str]]:
    """
    The score range each label covers. Your README needs these beside the
    label text — given to you so the numbers can't drift apart from config.py.
    """
    return [
        ("high-confidence human", f"0.00 – {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]
