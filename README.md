# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

Provenance Guard is a small Flask service a writing site can call to estimate
whether a piece of text was written with AI. It never makes a confident claim
on weak evidence, and every answer comes with a way to appeal. The path a
submission takes:

1. **It arrives.** The site sends `POST /submit` with `{"text", "creator_id"}`.
2. **It's checked.** Missing, blank, non-string or over-10,000-character input
   is refused (400 / 413), as is text too short to score (422). Each refusal
   writes a `rejected` entry to the audit log and nothing else.
3. **It gets an ID.** A fresh `content_id` ties the decision, the log and any
   appeal together.
4. **Signal one reads it.** GPT-2, running locally, measures how predictable
   the text is (`model_score`).
5. **Signal two measures its shape.** Sentence-length spread, vocabulary
   variety and punctuation (`style_score`).
6. **One number, then words.** `combine_signals` averages the two and keeps
   the result unsure if they disagree or the text is short. `score_to_label`
   turns it into `human` / `unsure` / `ai` and a plain-English sentence.
7. **It's logged and answered.** All nine fields go to `logs/audit.jsonl`, and
   the JSON response goes back with the label and the `content_id`.

If the writer disagrees, `POST /appeal` with that `content_id` and their
reasons records the appeal beside the original decision and moves the item to
`under_review`. Full trace, including the false-positive walkthrough:
`notes/milestone1.md`.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to GPT-2, running locally.
Perplexity is turned into a 0–1 score where more predictable means higher
(more AI-like). `detector.py::model_signal`, unchanged from the starter.

**Why that might differ between human and AI writing:** A language model writes
by choosing likely next words, so its output is easy for another model to
predict. People take odd turns, use specific details and make unexpected word
choices.

**What it can't see:** Who wrote it. It measures ordinariness, not authorship.
Plain, tidy writing (common words, short even sentences) scores as AI: the
Milestone 1 garden paragraph gets 0.79. Light edits to AI text push it the other
way: two edited AI texts dropped from about 0.85 to about 0.44.

### Signal two — the style signal

**What it measures:** The shape of the text, not its meaning
(`stylometry.py::style_signal`). Three measures, each mapped to 0–1 AI-ness
with a ramp set from calibration, then averaged equally:

| Measure | What it is | AI end → human end |
|---|---|---|
| Sentence-length spread | std ÷ mean of words per sentence | 0.20 → 0.60 (even = AI) |
| Vocabulary variety | type-token ratio over 50-word windows (MATTR) | 0.92 → 0.80 (*varied* = AI) |
| Varied punctuation | ; : ( ) — ' " ! ? etc. per 100 words, not . or , | 0.5 → 6.0 (sparse = AI) |

Under 3 sentences or 50 words it returns 0.5, meaning no opinion.

**Why that might differ between human and AI writing:** Generated prose
averages out the bumps: even, mid-length sentences, no asides, tidy
punctuation. One surprise from calibration: AI text had *more* varied
vocabulary than human text (0.88–0.94 vs 0.76–0.95), because people repeat
"I", "it" and the thing they're discussing, and assistant prose avoids
repeating itself. So that measure points the opposite way to the usual
assumption.

**What it can't see:** What the text says. Anything that changes the shape
without changing the content moves it: splitting or joining sentences,
adding dashes, brackets or a typo. It's also blind on short text, and a
comma-spliced paragraph counts as one sentence.

### The combining rule

**The rule:** Average the two signals with equal weight. If they're more than
0.40 apart, or the text is under 3 sentences or 50 words, keep the result
inside the unsure band. A confident label needs both signals pointing the
same way and enough text to judge.

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.5`, `WEIGHT_STYLE_SIGNAL = 0.5`,
`DISAGREEMENT_GAP = 0.40` (all in `config.py`). `MIN_SENTENCES = 3`,
`MIN_WORDS = 50` (in `stylometry.py`). Calibration (`python calibrate.py`):
clearly AI averages 0.845 (5 of 6 at or above 0.80), real human comments
average 0.34–0.37 (0 of 24 at or above 0.80).

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:**
A real r/csmajors comment ("This is cope. People from prestigious
schools…") scored `model_score` 0.515 and `style_score` 0.105: the model at
a coin flip, style confident it's human. The average, 0.31, is unsure. The gap
(0.41) also trips the disagreement rule, which would keep it unsure even if the
weights shifted toward style. Style alone would have called it human. The
average keeps either signal from deciding on its own.

One honest note: with equal weights and thresholds of 0.20 / 0.80, an average
of 0.80 or more already requires both signals to be at least 0.60. So the
disagreement rule can't change a label by itself today. It's kept as a guard
for when the weights or thresholds change. The short-text rule does change
outcomes. Full notes: `notes/milestone4.md`.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.20 (inclusive) | This looks like it was written by a person. If you think we got that wrong, you can ask for a review. |
| unsure | above 0.20, below 0.80 | We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review. |
| high-confidence AI | 0.80 – 1.00 (inclusive) | This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it. |

All three are reachable through `/submit`: a real r/csmajors comment scored
0.168 (human), the plainly written garden paragraph scored 0.679 (unsure), and
an AI-written paragraph scored 0.896 (AI). The bands meet with no gap: 0.20 is
human, 0.2001 is unsure, 0.80 is AI.

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

The person reading "unsure" may well have written every word, so it has to do
three things: say plainly that the service doesn't know, say that this is
*common* (and name the writing it happens to most, short or plain pieces) so
it doesn't feel like being singled out, and say outright that "it isn't an
accusation". It ends with the review option worded as an offer ("if you'd
like a person to take a look"), not a defence.

All three labels mention a review, not just the AI one, so asking for one
never signals guilt. The AI label also admits "our check can be wrong",
because at a 0.80 threshold it sometimes will be.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

Run on port 5050 (`PORT=5050 python app.py`) because macOS AirPlay Receiver
holds port 5000 on my machine. The text is a plainly written test paragraph,
the kind the model signal over-scores.

```bash
$ curl -X POST http://127.0.0.1:5050/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "My grandmother had a garden behind her house. Every summer we picked tomatoes and beans with her. She told us the names of all the plants. I did not like the work very much, but I liked being with her. Now I have my own garden, and I think about her when I am in it.", "creator_id": "austin"}'
```

```json
{
    "combined_score": 0.6792,
    "confidence": 0.3584,
    "content_id": "4ce1d472-a25b-415f-8887-acad25751ee2",
    "guess": "unsure",
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "model_score": 0.7901,
    "status": "decided",
    "style_score": 0.5682
}
```

The model signal alone (0.79) would be close to an accusation. Style (0.57)
reads it as more human, and the combined 0.68 lands in unsure.

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5050/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "4ce1d472-a25b-415f-8887-acad25751ee2", "reasoning": "I wrote this myself about my grandmother'"'"'s garden. I'"'"'d like a person to review it."}'
```

```json
{
    "content_id": "4ce1d472-a25b-415f-8887-acad25751ee2",
    "message": "Thanks, we've received your appeal. A person will review it. Until then the original label stays as it is, and we've kept a record of your reasons alongside it.",
    "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5050/log?limit=2"
```

```json
{
    "count": 2,
    "entries": [
        {
            "combined_score": 0.6792,
            "content_id": "4ce1d472-a25b-415f-8887-acad25751ee2",
            "creator_id": "austin",
            "guess": "unsure",
            "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
            "model_score": 0.7901,
            "status": "decided",
            "style_score": 0.5682,
            "timestamp": "2026-11-01T15:50:33+00:00"
        },
        {
            "content_id": "4ce1d472-a25b-415f-8887-acad25751ee2",
            "creator_id": "austin",
            "event": "appeal",
            "reasoning": "I wrote this myself about my grandmother's garden. I'd like a person to review it.",
            "status": "under_review",
            "timestamp": "2026-11-01T15:50:33+00:00"
        }
    ]
}
```

The original decision is untouched. The appeal sits after it with
`status: "under_review"`, and its `creator_id` was copied from the decision,
not taken from the request.

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
