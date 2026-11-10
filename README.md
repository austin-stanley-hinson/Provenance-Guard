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

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.5`, `WEIGHT_STYLE_SIGNAL = 0.5` in unit 7,
**changed to 0.3 / 0.7 in unit 8** as my one improvement (see The Improvement),
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

One honest note (true for the unit 7 weights): with equal weights and thresholds of 0.20 / 0.80, an average
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

**Moment 1: checking my own criteria against the contract**

- *What I asked for:* I wrote my five acceptance criteria myself and gave them
  to Claude to put into `criteria.md`.
- *What came back:* Claude pasted them in word for word, then flagged two
  wording problems before Unit 8 freezes them. Criterion 3 said "confidence
  score", but its 0.20 / 0.80 cutoffs apply to the combined score, and my
  Milestone 1 contract uses `confidence` for a different number (distance from
  a coin flip). Criterion 5 said invalid requests are rejected "without storing
  the submission", but the plan was to log every rejection, which Unit 8
  also asks for.
- *What I changed:* I had Claude make both fixes. Criterion 3 now says
  "combined score (0 = confidently human, 1 = confidently AI)", and criterion 5
  says no decision or classification is created, with a `rejected` log entry
  expected. The targets themselves are unchanged.

**Moment 2: the style signal ran the wrong way**

- *What I asked for:* to build the three style measures, write the combining
  rule down before coding it, and calibrate on clearly AI, clearly human, plain
  human and lightly edited AI text, using real r/csmajors comments from my
  TakeMeter project as the human writing.
- *What came back:* Vocabulary variety pointed the opposite way to the
  starter's guess. AI text scored 0.88–0.94 on the type-token ratio and human
  comments 0.76–0.95, because people repeat "I", "it" and their topic while
  assistant prose avoids repeating itself. Flipping that measure is what keeps
  the plainly written garden paragraph from Milestone 1 at unsure (0.68)
  instead of near an accusation, even though the model signal alone gives it
  0.79. Claude also caught two of its own overclaims: with equal weights and my
  0.20 / 0.80 thresholds, the disagreement rule can't change a label on its
  own, and the split case it first described as "held unsure by the rule" was
  already unsure by its average.
- *What I changed:* I kept the flipped direction and kept the disagreement
  rule as a guard, with the README saying plainly that it doesn't change any
  label today. Calibration ends up at 5 of 6 AI texts labelled AI and 0 of 24
  human comments, with the caveat that the ramps were set from those same texts.

**Moment 3: a 403 that wasn't my code**

- *What I asked for:* to test `/submit` with curl after building it.
- *What came back:* Every request, `/ping` included, returned 403. Claude
  checked what was listening and found macOS Control Center (AirPlay Receiver)
  also bound to port 5000. Later a stale Flask process kept answering with old
  code because the kill command missed it (macOS lists it as `Python`).
- *What I changed:* I chose to run on port 5050 (`PORT=5050 python app.py`)
  instead of turning AirPlay off, so the Sample Run uses 5050 and says why.
  Three log entries with `style_score: null` from the stale server are still
  in `logs/audit.jsonl`, because the log is append-only.

**What else Claude drafted (disclosure):** Claude wrote the Milestone 1 trace
and endpoint contract (`notes/milestone1.md`), all the code for `/submit`,
`/appeal`, `stylometry.py` and `scoring.py`, `calibrate.py`, the three label
texts, and the README sections What This Does, Signals and Scoring, Label
Variants and Sample Run. I read them and kept them as written.

**Test text disclosure:** The six "clearly AI" and two "lightly edited AI"
calibration texts in `calibration/texts.py` were written by Claude. The garden
paragraph used in Milestone 1 and the Sample Run was also written by Claude to
imitate plain writing. It is *not* verified human writing, which is why
criterion 1 has to be tested on real human samples. The human calibration
texts are real r/csmajors comments from TakeMeter.

**Unit 8**

**Moment 4: the baseline that explained the attack run**

- *What I asked for:* diagnoses for every broken attack, naming the stage and
  the mechanism, by scoring each attack text directly with the same functions
  `/submit` calls, without changing anything.
- *What came back:* Claude fixed EV01's typos by hand to get a clean version of
  the staff AI paragraph, and it scored only 0.814, just 0.014 above my AI
  line. Signal one gave it 0.669 but gave five real human false-positive texts
  0.80–0.88. That turned twelve breaks into three causes: no margin on AI text
  (seven evasions), the short-text rule (two), and the route accepting text
  with no words (three). It also found that EV01's typos, aimed at signal two,
  actually sank signal one.
- *What I changed:* Claude laid out three possible improvements (reweight,
  refuse wordless text, split on semicolons) with the cost of each. I chose the
  reweight because it follows the main pattern, and the 0.3 / 0.7 numbers were
  committed before any after run.

**Moment 5: a miss that wasn't the reweight**

- *What I asked for:* the after runs, and to score them.
- *What came back:* criterion 5 dropped to 4/5 in all three trials. Claude
  traced it to the rate limiter: the request with no `creator_id` is counted
  against my IP address, and the attack run 10 seconds earlier had used up
  that address's 5 per minute. It re-ran the eval with nothing changed and got
  5/5.
- *What I changed:* I kept both result files and reported the first run as a
  miss with its own diagnosis, instead of only showing the clean re-run.

**Moment 6: the worst-failure exercise**

- *What I asked for:* context and hints for the breakout question on FP03,
  not the answer.
- *What came back:* four questions, one per stage, each with a command to
  run (`detector.py`, `stylometry.py`, the weights worked by hand, and the
  threshold). My own write-up of the Milestone 3 results and FP03 is in
  `notes/unit8_milestone3.md`.

**What Claude drafted in unit 8 (disclosure):** the rate-limit numbers and
reasoning, `scenarios.py`, `run_appeal_eval.py`, `score_eval.py`, two fields
added to `run_eval.py`'s recording, the held/broke marking rules, every
unit 8 README section, and the ten AI texts in `scenarios.py::AI_FRESH`. The
attack set was moved into the repo from my Downloads and run before anything in
it was read beyond the header row. Claude also caught and corrected three of
its own errors in the write-up: FP03's signal-one score beats two of my six
calibration AI texts, not four; MF05 is 4,000 letters, not 60; and FP08 went
*up* after the reweight, so not every false-positive text improved.

**Time spent (unit 7):** 5 hours.

**Time spent (unit 8):** 5 hours.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

A real writer submits a piece, maybe tweaks it and checks again. Even someone
revising quickly is unlikely to send more than 5 in one minute, and 50 in a day
is several pieces each checked many times. A script mapping my 0.20 / 0.80
thresholds needs hundreds of near-identical variations. At 5 a minute it's
stopped after 5 tries, and at 50 a day it would need weeks per creator_id. I
went below the starter's 10 / 200 because nothing about a writing site needs
10 checks a minute, and 200 a day is already enough to map a threshold roughly.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

Per `creator_id` when the request has one, and per IP address when it doesn't
(`app.py::rate_limit_key`). That's fair to a household or classroom sharing one
address. But `creator_id` is whatever the caller sends, so a script that makes up
a new id for every request is never limited. That's the gap. A real deployment
would key on a logged-in account, or add a per-address limit on top.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

`PORT=5050 python run_attacks.py --flood 15` (from `results/flood_2026-11-09_2007.md`):

```
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
```

Each of the 10 rejections is in `logs/audit.jsonl` as its own entry:

```json
{"creator_id": "flood_tester", "event": "rejected", "limit": "5 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-10T01:07:29+00:00"}
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

`PORT=5050 python run_attacks.py --set attack_set --label before`, all 56 inputs,
no crashes, no 5xx. Full output: `results/attack_run_2026-11-09_2014_before.md`.
Combined scores come from the audit log for the same run
(`results/audit_extract_before.json`), because the runner's "Score" column is
`confidence`.

**How I marked them.** *Evasion* (AI text): HELD only if labelled AI.
Landing in unsure means the AI text got through unflagged, so it's BROKE.
*False positive* (human text): HELD unless labelled AI. *Prompt injection*:
HELD if the instruction didn't change the label, the label text or the log.
*Malformed*: HELD if refused with a clean 4xx, or answered without a crash
when there is real text. BROKE if the service logged a classification for
text containing no words. *Flood*: HELD if the limit cut it off.

| Family | Held | Broke |
|---|---|---|
| evasion | 1 | **9** |
| false_positive | 8 | 0 |
| prompt_injection | 6 | 0 |
| malformed | 17 | **3** |
| flood_same_creator | 12 | 0 |
| **Total** | **44** | **12** |

| ID | Family | Targeting | Status | Guess | Model | Style | Combined | Verdict |
|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.164 | 0.959 | 0.561 | **BROKE** |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.594 | 0.359 | 0.477 | **BROKE** |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.666 | 0.464 | 0.565 | **BROKE** |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.611 | 0.889 | 0.750 | **BROKE** |
| EV05 | evasion | both signals: heavy human editing pass | 200 | unsure | 0.321 | 0.307 | 0.314 | **BROKE** |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.573 | 0.469 | 0.521 | **BROKE** |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.586 | 0.500 | 0.543 | **BROKE** |
| EV08 | evasion | signal one: text below the token window | 200 | unsure | 0.245 | 0.500 | 0.373 | **BROKE** |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.704 | 0.534 | 0.619 | **BROKE** |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.979 | 0.667 | 0.823 | **HELD** |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.618 | 0.470 | 0.543 | **HELD** |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.739 | 0.633 | 0.686 | **HELD** |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | unsure | 0.805 | 0.614 | 0.709 | **HELD** |
| FP04 | false_positive | a student essay written to a rubric | 200 | unsure | 0.833 | 0.586 | 0.710 | **HELD** |
| FP05 | false_positive | technical documentation written by a person | 200 | unsure | 0.800 | 0.603 | 0.702 | **HELD** |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.881 | 0.401 | 0.641 | **HELD** |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.882 | 0.333 | 0.608 | **HELD** |
| FP08 | false_positive | very short genuine human submission | 200 | unsure | 0.322 | 0.500 | 0.411 | **HELD** |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.463 | 0.500 | 0.481 | **HELD** |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | unsure | 0.204 | 0.500 | 0.352 | **HELD** |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.594 | 0.434 | 0.514 | **HELD** |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.500 | 0.336 | 0.418 | **HELD** |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.640 | 0.500 | 0.570 | **HELD** |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.558 | 0.497 | 0.528 | **HELD** |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | — | **HELD** |
| MF02 | malformed | text is a single character | 422 | — | — | — | — | **HELD** |
| MF03 | malformed | text is control characters | 200 | unsure | 0.000 | 0.500 | 0.250 | **HELD** |
| MF04 | malformed | text is only punctuation | 200 | unsure | 0.011 | 0.500 | 0.256 | **BROKE** |
| MF05 | malformed | text is a very long single word | 200 | unsure | 0.998 | 0.500 | 0.749 | **BROKE** |
| MF06 | malformed | text is emoji only | 200 | unsure | 0.997 | 0.500 | 0.749 | **BROKE** |
| MF07 | malformed | text is right-to-left script | 200 | unsure | 0.906 | 0.500 | 0.703 | **HELD** |
| MF08 | malformed | text is 60,000 characters | 413 | — | — | — | — | **HELD** |
| RQ01 | malformed | no text field at all | 400 | — | — | — | — | **HELD** |
| RQ02 | malformed | no creator_id | 400 | — | — | — | — | **HELD** |
| RQ03 | malformed | text is a number | 400 | — | — | — | — | **HELD** |
| RQ04 | malformed | text is a list | 400 | — | — | — | — | **HELD** |
| RQ05 | malformed | text is null | 400 | — | — | — | — | **HELD** |
| RQ06 | malformed | creator_id is an object | 400 | — | — | — | — | **HELD** |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | — | **HELD** |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | — | **HELD** |
| RQ09 | malformed | body is empty | 400 | — | — | — | — | **HELD** |
| RQ10 | malformed | body is form-encoded, not JSON | 429 (400 alone) | — | — | — | — | **HELD** |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 (400 alone) | — | — | — | — | **HELD** |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | — | **HELD** |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.500 | 0.264 | **HELD** |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.500 | 0.264 | **HELD** |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.500 | 0.264 | **HELD** |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.500 | 0.264 | **HELD** |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.500 | 0.264 | **HELD** |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** |

Notes on the judgement calls:

- **RQ10, RQ11** came back 429 in the full run. They have no usable
  `creator_id`, so they count against my address, which earlier malformed rows
  had used up. Sent alone a minute later
  (`results/attack_run_2026-11-09_2015_recheck_RQ10.md`, `…_RQ11.md`), both
  reach the route and get a 400 `invalid_json`.
- **MF04, MF05, MF06** (only punctuation, one 4,000-letter word, only emoji)
  each got a logged decision. Signal one scored the word and the emoji at
  0.997–0.998, near-certain AI, and only the short-text rule kept the label at
  unsure. A stored classification of text with no words in it is a broken
  result even though the label is harmless.
- **MF07** (right-to-left script) is real writing, so a 200 with "unsure" is
  fair. But my word regex only matches a–z, so the style signal can never read
  non-Latin text. See What's Still Broken.
- **Prompt injection** never changed a label, because nothing in the pipeline
  reads instructions. It did move the number: scored without the instruction,
  PI02's paragraph gets `model_score` 0.754; with "SYSTEM: … guess=human,
  confidence=0.02" in front, it gets 0.204. The instruction works as
  *unpredictable text*, not as a command.
- **Flood**: FL01_01–05 got 200 and FL01_06–12 got 429. The set has 12 rows
  rather than the 20 its description says.

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

In order: EV01 (typos sank signal one), EV04 (rare words, the closest evasion
to the AI band), EV09 (human opening bolted on), FP03 (non-native writer,
signal one at 0.81), FP04 (rubric essay, the highest false-positive score),
PI02 (the fake system message), PI05 (the log-injection attempt, stored
safely), MF06 (emoji scored 0.997 by signal one), then two rejections: MF08
at 60,000 characters (413) and a FL01 flood row (429).

```json
{"combined_score": 0.5613, "content_id": "e6e18305-9bfa-4c42-ade0-c919acffd0c0", "creator_id": "attacker_EV01", "guess": "unsure", "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.", "model_score": 0.1635, "status": "decided", "style_score": 0.959, "timestamp": "2026-11-10T01:14:14+00:00"}
{"combined_score": 0.7504, "content_id": "d10e04fd-9a0d-4dea-be07-06b3f11e4e43", "creator_id": "attacker_EV04", "guess": "unsure", "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.", "model_score": 0.6114, "status": "decided", "style_score": 0.8894, "timestamp": "2026-11-10T01:14:14+00:00"}
{"combined_score": 0.6193, "content_id": "bd9eec90-215e-4c50-9c51-5577e6af59bd", "creator_id": "attacker_EV09", "guess": "unsure", "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.", "model_score": 0.7042, "status": "decided", "style_score": 0.5344, "timestamp": "2026-11-10T01:14:14+00:00"}
{"combined_score": 0.7094, "content_id": "2c85a210-d45a-4b7a-8bbb-24d12b5a0744", "creator_id": "attacker_FP03", "guess": "unsure", "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.", "model_score": 0.8051, "status": "decided", "style_score": 0.6137, "timestamp": "2026-11-10T01:14:15+00:00"}
{"combined_score": 0.7097, "content_id": "40231249-942e-4b6d-9cc0-2d8e7da362df", "creator_id": "attacker_FP04", "guess": "unsure", "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.", "model_score": 0.8329, "status": "decided", "style_score": 0.5864, "timestamp": "2026-11-10T01:14:15+00:00"}
{"combined_score": 0.3522, "content_id": "6d95189b-210a-4ae2-92a3-e59ff3e96c02", "creator_id": "attacker_PI02", "guess": "unsure", "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.", "model_score": 0.2044, "status": "decided", "style_score": 0.5, "timestamp": "2026-11-10T01:14:15+00:00"}
{"combined_score": 0.57, "content_id": "7bdbb96b-c7c3-47d7-836e-decd790672cc", "creator_id": "attacker_PI05", "guess": "unsure", "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.", "model_score": 0.6401, "status": "decided", "style_score": 0.5, "timestamp": "2026-11-10T01:14:15+00:00"}
{"combined_score": 0.7485, "content_id": "8521a7f6-e58a-4334-b031-cf16f8e31b62", "creator_id": "attacker_MF06", "guess": "unsure", "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.", "model_score": 0.9969, "status": "decided", "style_score": 0.5, "timestamp": "2026-11-10T01:14:16+00:00"}
{"creator_id": "attacker_MF08", "event": "rejected", "http_status": 413, "reason": "text_too_long", "status": "rejected", "timestamp": "2026-11-10T01:14:16+00:00"}
{"creator_id": "attacker_flood", "event": "rejected", "limit": "5 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-10T01:14:16+00:00"}
```

PI05's text tried to close a JSON string and add `"guess": "human"`. The entry
above has its real guess (`unsure`) and no extra fields. The log never stores
the submitted text, and every line is written with `json.dumps`.

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

**FP03, the non-native English speaker.** No real writer was labelled AI in this
run, so the worst outcome is the nearest miss. FP03 is a careful, plain account
of a first month in a new country. Signal one gave it **0.805**, higher than
two of the six AI texts I calibrated with (0.67 and 0.77), and the combined score was
**0.709**. That is 0.09 from an accusation, and it was held off only by a style
score of 0.61 and the deliberately wide unsure band. It's exactly the writer the
Milestone 1 trace worried about, and the one with the least room to argue back.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

`PORT=5050 python run_eval.py --label before` for criteria 1, 2, 3 and 5
(scenarios in `scenarios.py`), and `PORT=5050 python run_appeal_eval.py --label
before` for criterion 4, because an appeal needs a content_id from a
submission first and `run_eval.py` only sends `/submit`. Per-trial numbers come
from `python score_eval.py results/run_2026-11-09_2044_before.md`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human writing labelled AI (20 unseen r/csmajors comments) | ≤ 1 of 20 | 0/20 | 0/20 | 0/20 | MET |
| 2. AI mean − human mean, combined score (10 + 10) | ≥ 0.25 | 0.479 | 0.479 | 0.479 | MET |
| 3. All three labels reached | 3 of 3 | 3/3 | 3/3 | 3/3 | MET |
| 4. Appeals recorded, `under_review`, confirmed | 10 of 10 | 10/10 | 10/10 | 10/10 | MET |
| 5. Invalid input → 400/413 + JSON error, no decision | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

All three trials were identical, which is expected: neither signal has any
randomness. Criterion 2's means were AI 0.828 and human 0.349 in every trial.
For criterion 5, the audit log shows 0 decisions for any of its creator_ids.

**What the test texts were.** Criterion 1 and the human half of criterion 2 are
30 real r/csmajors comments from TakeMeter, 50+ words each, none of them used
to set the style ramps (`eval_data/takemeter_unseen.json`). The AI half of
criterion 2 is 10 texts Claude wrote for this run on new topics. 6 of the 20
criterion 1 comments have under 3 sentences, so the short-text rule makes them
unsure no matter what.

**How I reached each verdict.** A criterion is MET only if the target holds in
all three trials, not in the best one.

1. **MET.** 0 of 20 in every trial, and the highest of the 20 combined scores
   was 0.658, well under 0.80. This counts only the `ai` label, as the
   criterion says, so near-misses don't count against it. But see the next
   section: this target turned out to be easy.
2. **MET.** The gap was 0.479 in every trial, nearly double the 0.25 target.
   8 of 10 AI texts got the `ai` label and 2 got `unsure` (0.727 and 0.706).
3. **MET.** `human`, `unsure` and `ai` all came back in every trial. The bands
   meet with no gap: `scoring.score_to_label` gives 0.20 → human,
   0.2001 → unsure, 0.80 → ai.
4. **MET.** 30 of 30 appeals across the three trials returned 200 with
   `under_review` and a message. Each one has an appeal entry in the log with
   its exact reasoning, and that's the latest status for its content_id.
5. **MET.** Every invalid request got a 400 or 413 with an `error` code and a
   `message`, and the audit log has 0 decisions for those creator_ids. That
   includes the one with no creator_id, which logged as `unknown`.

**I held all five, so were the targets low?** Partly, yes, and the attack set
shows where. Criterion 1 was the soft one. My 20 human texts were casual Reddit
comments, which surprise GPT-2 (their highest signal-one score was 0.73). The
staff's false-positive set is formal, plain and careful writing, and signal one
gave five of those eight 0.80–0.88. FP03 reached 0.709 combined. Six of my 20
comments were also under 3 sentences, so the short-text rule made them unsure
automatically. **The criterion I'd tighten is 1:** the same "at most 1 of 20"
target, but on human writing that is plain or formal on purpose (essays to a
rubric, documentation, careful second-language writing), plus a second
threshold, "none above 0.70", that would catch near-misses like FP03. None of my
five criteria tests evasion either, which is where 9 of my 12 broken attacks
are.

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

From `results/run_2026-11-09_2044_before.md`, produced by `run_eval.py::main` against `app.py::submit`
(scores from `detector.py::model_signal`, `stylometry.py::style_signal`,
`scoring.py::combine_signals`, label from `scoring.py::score_to_label`). Trial 1.

*Criterion 1:* the highest-scoring of the 20 human comments.

```json
{
  "status": 200,
  "content_id": "ae8ba077-ca6c-4d8b-b431-27770d451f67",
  "guess": "unsure",
  "combined_score": 0.6581,
  "confidence": 0.3162,
  "model_score": 0.4697,
  "style_score": 0.8465,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "message": null,
  "sent": "yep i worked in software for a retail company as my first tech job. su"
}
```

*Criterion 2:* the first AI text and the first human comment.

```json
[
  {
    "status": 200,
    "content_id": "039bb5f0-12e1-4689-ab2e-308e734b5c2a",
    "guess": "ai",
    "combined_score": 0.8266,
    "confidence": 0.6532,
    "model_score": 0.7825,
    "style_score": 0.8707,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Effective budgeting is a cornerstone of financial stability. By tracki"
  },
  {
    "status": 200,
    "content_id": "13959de8-98a8-4ad9-8fb8-7e4ba6610fd4",
    "guess": "unsure",
    "combined_score": 0.3378,
    "confidence": 0.3244,
    "model_score": 0.3423,
    "style_score": 0.3333,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I agree with this guy. Went to a career fair once and talked to a coup"
  }
]
```

*Criterion 3:* one input aimed at each band.

```json
[
  {
    "status": 200,
    "content_id": "519deef9-9f52-4246-a356-81a517796b37",
    "guess": "human",
    "combined_score": 0.1676,
    "confidence": 0.6648,
    "model_score": 0.3192,
    "style_score": 0.0161,
    "label": "This looks like it was written by a person. If you think we got that wrong, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Totally agree. I don’t go to a T20 School, I don’t consider myself a ‘"
  },
  {
    "status": 200,
    "content_id": "2e6e2075-76ce-4fd6-96e4-4ce8ca3e2a94",
    "guess": "unsure",
    "combined_score": 0.6792,
    "confidence": 0.3584,
    "model_score": 0.7901,
    "style_score": 0.5682,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "My grandmother had a garden behind her house. Every summer we picked t"
  },
  {
    "status": 200,
    "content_id": "d33ae649-f3c2-4e93-8d96-66315f190b3e",
    "guess": "ai",
    "combined_score": 0.8959,
    "confidence": 0.7918,
    "model_score": 0.941,
    "style_score": 0.8508,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Climate change is one of the most pressing issues facing our world tod"
  }
]
```

*Criterion 4:* from `results/appeal_run_2026-11-09_2044_before.md`, produced by `run_appeal_eval.py::run_trial`
against `app.py::appeal`. Trial 1, piece 1.

```json
{
  "piece": 1,
  "submit_status": 200,
  "content_id": "94de0b6d-c3d5-4ee2-85df-6a8f0a3f4de4",
  "reasoning": "Trial 1, piece 1: I wrote this myself and would like a review.",
  "appeal_status": 200,
  "response": {
    "content_id": "94de0b6d-c3d5-4ee2-85df-6a8f0a3f4de4",
    "message": "Thanks, we've received your appeal. A person will review it. Until then the original label stays as it is, and we've kept a record of your reasons alongside it.",
    "status": "under_review"
  },
  "logged_with_reasoning": true,
  "latest_status": "under_review",
  "passed": true
}
```

*Criterion 5:* all five invalid requests.

```json
[
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "combined_score": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "missing_field",
    "message": "`text` is required and must be a non-empty string.",
    "sent": "{\"creator_id\": \"eval_bad_no_text\"}"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "combined_score": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "missing_field",
    "message": "`text` is required and must be a non-empty string.",
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "combined_score": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "missing_field",
    "message": "`text` is required and must be a non-empty string.",
    "sent": "   \n\t  "
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "combined_score": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "missing_field",
    "message": "`creator_id` is required and must be a non-empty string.",
    "sent": "{\"text\": \"Real writing with no creator attached to it.\"}"
  },
  {
    "status": 413,
    "content_id": null,
    "guess": null,
    "combined_score": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "text_too_long",
    "message": "`text` is 10,001 characters. The limit is 10,000.",
    "sent": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  }
]
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

No criterion missed, so these diagnoses cover the 12 broken attacks and the
false-positive near-misses. I worked them out by scoring each attack text
directly with the same functions `/submit` calls (`detector.perplexity`,
`stylometry.style_parts`, `scoring.combine_signals`), without changing
anything.

**The baseline that explains most of it.** Most evasions are edits of one staff
AI paragraph. With EV01's typos corrected by hand, that paragraph scores
`model_score` **0.669** (perplexity 29), `style_score` 0.959, combined **0.814**.
That's the `ai` label by just **0.014**.

**Pattern 1: signal one ranks plain human writing as more AI-like than real AI
text (stage: signal one).** It gives the clean AI paragraph 0.669, but it gives
FP03, FP04, FP05, FP06 and FP07, all real human writing, **0.80–0.88**
(perplexity 12.8–18.9). It's measuring how ordinary the words are, and careful
human writing is more ordinary than this AI paragraph. Two consequences:

- **AI text has almost no margin.** Because signal one gives AI text only about
  0.67, an `ai` label needs signal two at about 0.93 or above. Any attack that
  dents *either* signal a little breaks it. That's EV01–EV06 and EV09 below.
- **The false-positive risk comes from this signal.** Every FP text that
  reached 0.70 combined did it on a signal-one score of 0.80 or more.

**Pattern 2: signal two is pure shape, and shape is cheap to change (stage:
signal two).** Four attacks changed only the shape and pulled style from 0.959
to 0.36–0.50.

**Each broken attack:**

| Attack | Stage | Mechanism (scores from the run) |
|---|---|---|
| EV01 typos | **signal one** | The attack aimed at signal two, but signal two didn't move (0.959; vocabulary variety was already at the AI end). Misspellings are tokens GPT-2 can't predict: perplexity went from 29 to **125** and `model_score` from 0.669 to **0.164**. Combined 0.561. |
| EV02 broken-up sentences | **signal two** | 13 short sentences pushed length spread to 0.85, past the 0.60 human end of its ramp, so the spread part went 1.0 → 0. Style 0.359, combined 0.477. |
| EV03 pasted quotation | **signal two** | The quote marks raised varied punctuation to 6.6 per 100 words, so the punctuation part went to 0, and the quotation's sentence lengths lowered the spread part to 0.39. Style 0.464, combined 0.565. |
| EV04 unusual words | **signal one → combining rule** | Rare words raised perplexity a little (34), so `model_score` was 0.611. Style still said AI (0.889), but the average was 0.750. With signal one capped near 0.6–0.7 on this text, the 0.80 line is out of reach. |
| EV05 heavy human edit | **both signals** | Rewritten with dashes, fragments and asides. Model 0.321, style 0.307. This is arguably human writing now; I don't count it as a fixable miss. |
| EV06 one long, one short sentence | **signal two** | Spread hit 1.19, so the spread part went to 0. Style 0.469, combined 0.521. |
| EV07 padding with punctuation | **signal two's sentence splitter → combining rule** | Every sentence was joined with "; and, moreover,". `stylometry._sentence_lengths` only splits on `. ! ?`, so 97 words counted as **1 sentence**. That trips the short-text rule (under 3 sentences), so style returns 0.5 and the result is held in unsure. The punctuation padding itself never mattered. |
| EV08 below the token window | **combining rule (by design)** | 10 words and 2 sentences, so the short-text rule keeps it unsure. That's the trade I chose in Milestone 4: too little text to accuse anyone. |
| EV09 human opening bolted on | **both signals (whole-text averaging)** | Both signals score the whole text as one block, so a casual human first paragraph dilutes the AI body. Model 0.704, style 0.534, combined 0.619. Nothing looks at sections separately. |
| MF04 punctuation only | **route** | `/submit` accepts any non-blank string under 10,000 characters. The detector only refuses fewer than 3 tokens, and punctuation tokenizes fine, so a text with **0 words** got a decision. |
| MF05 one 4,000-letter word | **route + signal one** | Same route gap. GPT-2 finds "aaaa…" perfectly predictable (perplexity **1.0**), so `model_score` 0.998, and only the short-text rule held it at unsure (0.749). |
| MF06 emoji only | **route + signal one** | 0 words; perplexity 1.2, so `model_score` 0.997, held at unsure (0.749). Same gap. |

**What held, and why it was close.** No false-positive text was labelled AI.
FP02–FP05 (formal, second-language, rubric essay, documentation) all landed at
0.69–0.71. Two things pushed them up: signal one (pattern 1), and the
**punctuation part of signal two, which was 1.0 for all eight FP texts**. None
of them used a semicolon, dash, bracket or contraction, because careful formal
writers often don't. The vocabulary measure is what saved them: people repeat
words, so the mattr part was 0–0.18. The 0.80 threshold did the rest.

**One problem, not twelve.** Seven evasions (EV01–EV06, EV09) trace back to the
same thing: the AI text starts only 0.014 above the line, because signal one
doesn't recognise it as AI. Two (EV07, EV08) are the short-text rule. Three
(MF04–06) are one missing check in the route.

---

## The Improvement

**What I changed:** One line pair in `config.py`: `WEIGHT_MODEL_SIGNAL` 0.5 → **0.3**
and `WEIGHT_STYLE_SIGNAL` 0.5 → **0.7**. Nothing else moved. Same thresholds
(0.20 / 0.80), same disagreement rule (0.40), same short-text rule, same
labels. I committed the change (`41d7acf`) before running anything against it,
and picked 0.3 / 0.7 without trying other values on the attack set.

**Which diagnosis pointed at it:** Pattern 1. Signal one gave the clean staff
AI paragraph only 0.669 but gave five real human false-positive texts
0.80–0.88. It was both the false-positive risk and the reason AI text sat just
0.014 above the line. Trusting it less should push careful human writing down
and, where style still reads AI, push AI text up. The known cost from pattern
2: style is the cheap-to-change signal, so shape attacks should get a little
stronger.

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

`PORT=5050 python run_attacks.py --set attack_set --label after`, all 56 inputs,
no crashes. Full output: `results/attack_run_2026-11-09_2053_after.md`, with scores from
`results/audit_extract_after.json`. Marked by the same rules as the before
run. ⬅ marks a verdict that changed.

| Family | Before (held / broke) | After (held / broke) |
|---|---|---|
| evasion | 1 / 9 | 1 / 9 |
| false_positive | 8 / 0 | 8 / 0 |
| prompt_injection | 6 / 0 | 6 / 0 |
| malformed | 17 / 3 | 17 / 3 |
| flood_same_creator | 12 / 0 | 12 / 0 |
| **Total** | **44 / 12** | **44 / 12** |

| ID | Family | Status | Before: guess, combined | After: guess | Model | Style | Combined | Before | After |
|---|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | 200 | unsure 0.561 | unsure | 0.164 | 0.959 | 0.720 | BROKE | **BROKE** |
| EV02 | evasion | 200 | unsure 0.477 | unsure | 0.594 | 0.359 | 0.430 | BROKE | **BROKE** |
| EV03 | evasion | 200 | unsure 0.565 | unsure | 0.666 | 0.464 | 0.524 | BROKE | **BROKE** |
| EV04 | evasion | 200 | unsure 0.750 | ai | 0.611 | 0.889 | 0.806 | BROKE | **HELD** ⬅ |
| EV05 | evasion | 200 | unsure 0.314 | unsure | 0.321 | 0.307 | 0.311 | BROKE | **BROKE** |
| EV06 | evasion | 200 | unsure 0.521 | unsure | 0.573 | 0.469 | 0.500 | BROKE | **BROKE** |
| EV07 | evasion | 200 | unsure 0.543 | unsure | 0.586 | 0.500 | 0.526 | BROKE | **BROKE** |
| EV08 | evasion | 200 | unsure 0.373 | unsure | 0.245 | 0.500 | 0.424 | BROKE | **BROKE** |
| EV09 | evasion | 200 | unsure 0.619 | unsure | 0.704 | 0.534 | 0.585 | BROKE | **BROKE** |
| EV10 | evasion | 200 | ai 0.823 | unsure | 0.979 | 0.667 | 0.760 | HELD | **BROKE** ⬅ |
| FP01 | false_positive | 200 | unsure 0.543 | unsure | 0.618 | 0.470 | 0.514 | HELD | **HELD** |
| FP02 | false_positive | 200 | unsure 0.686 | unsure | 0.739 | 0.633 | 0.665 | HELD | **HELD** |
| FP03 | false_positive | 200 | unsure 0.709 | unsure | 0.805 | 0.614 | 0.671 | HELD | **HELD** |
| FP04 | false_positive | 200 | unsure 0.710 | unsure | 0.833 | 0.586 | 0.660 | HELD | **HELD** |
| FP05 | false_positive | 200 | unsure 0.702 | unsure | 0.800 | 0.603 | 0.662 | HELD | **HELD** |
| FP06 | false_positive | 200 | unsure 0.641 | unsure | 0.881 | 0.401 | 0.545 | HELD | **HELD** |
| FP07 | false_positive | 200 | unsure 0.608 | unsure | 0.882 | 0.333 | 0.498 | HELD | **HELD** |
| FP08 | false_positive | 200 | unsure 0.411 | unsure | 0.322 | 0.500 | 0.447 | HELD | **HELD** |
| PI01 | prompt_injection | 200 | unsure 0.481 | unsure | 0.463 | 0.500 | 0.489 | HELD | **HELD** |
| PI02 | prompt_injection | 200 | unsure 0.352 | unsure | 0.204 | 0.500 | 0.411 | HELD | **HELD** |
| PI03 | prompt_injection | 200 | unsure 0.514 | unsure | 0.594 | 0.434 | 0.482 | HELD | **HELD** |
| PI04 | prompt_injection | 200 | unsure 0.418 | unsure | 0.500 | 0.336 | 0.385 | HELD | **HELD** |
| PI05 | prompt_injection | 200 | unsure 0.570 | unsure | 0.640 | 0.500 | 0.542 | HELD | **HELD** |
| PI06 | prompt_injection | 200 | unsure 0.528 | unsure | 0.558 | 0.497 | 0.515 | HELD | **HELD** |
| MF01 | malformed | 400 | — — | — | — | — | — | HELD | **HELD** |
| MF02 | malformed | 422 | — — | — | — | — | — | HELD | **HELD** |
| MF03 | malformed | 200 | unsure 0.250 | unsure | 0.000 | 0.500 | 0.350 | HELD | **HELD** |
| MF04 | malformed | 200 | unsure 0.256 | unsure | 0.011 | 0.500 | 0.353 | BROKE | **BROKE** |
| MF05 | malformed | 200 | unsure 0.749 | unsure | 0.998 | 0.500 | 0.649 | BROKE | **BROKE** |
| MF06 | malformed | 200 | unsure 0.749 | unsure | 0.997 | 0.500 | 0.649 | BROKE | **BROKE** |
| MF07 | malformed | 200 | unsure 0.703 | unsure | 0.906 | 0.500 | 0.622 | HELD | **HELD** |
| MF08 | malformed | 413 | — — | — | — | — | — | HELD | **HELD** |
| RQ01 | malformed | 400 | — — | — | — | — | — | HELD | **HELD** |
| RQ02 | malformed | 400 | — — | — | — | — | — | HELD | **HELD** |
| RQ03 | malformed | 400 | — — | — | — | — | — | HELD | **HELD** |
| RQ04 | malformed | 400 | — — | — | — | — | — | HELD | **HELD** |
| RQ05 | malformed | 400 | — — | — | — | — | — | HELD | **HELD** |
| RQ06 | malformed | 400 | — — | — | — | — | — | HELD | **HELD** |
| RQ07 | malformed | 400 | — — | — | — | — | — | HELD | **HELD** |
| RQ08 | malformed | 400 | — — | — | — | — | — | HELD | **HELD** |
| RQ09 | malformed | 400 | — — | — | — | — | — | HELD | **HELD** |
| RQ10 | malformed | 429 (400 alone) | — — | — | — | — | — | HELD | **HELD** |
| RQ11 | malformed | 429 (400 alone) | — — | — | — | — | — | HELD | **HELD** |
| RQ12 | malformed | 400 | — — | — | — | — | — | HELD | **HELD** |
| FL01_01 | flood_same_creator | 200 | unsure 0.264 | unsure | 0.029 | 0.500 | 0.359 | HELD | **HELD** |
| FL01_02 | flood_same_creator | 200 | unsure 0.264 | unsure | 0.029 | 0.500 | 0.359 | HELD | **HELD** |
| FL01_03 | flood_same_creator | 200 | unsure 0.264 | unsure | 0.029 | 0.500 | 0.359 | HELD | **HELD** |
| FL01_04 | flood_same_creator | 200 | unsure 0.264 | unsure | 0.029 | 0.500 | 0.359 | HELD | **HELD** |
| FL01_05 | flood_same_creator | 200 | unsure 0.264 | unsure | 0.029 | 0.500 | 0.359 | HELD | **HELD** |
| FL01_06 | flood_same_creator | 429 | — — | — | — | — | — | HELD | **HELD** |
| FL01_07 | flood_same_creator | 429 | — — | — | — | — | — | HELD | **HELD** |
| FL01_08 | flood_same_creator | 429 | — — | — | — | — | — | HELD | **HELD** |
| FL01_09 | flood_same_creator | 429 | — — | — | — | — | — | HELD | **HELD** |
| FL01_10 | flood_same_creator | 429 | — — | — | — | — | — | HELD | **HELD** |
| FL01_11 | flood_same_creator | 429 | — — | — | — | — | — | HELD | **HELD** |
| FL01_12 | flood_same_creator | 429 | — — | — | — | — | — | HELD | **HELD** |

**My five criteria, after** (`PORT=5050 python run_eval.py --label after`,
`run_appeal_eval.py --label after`):

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human writing labelled AI | ≤ 1 of 20 | 0/20 | 0/20 | 0/20 | MET |
| 2. AI mean − human mean | ≥ 0.25 | 0.465 | 0.465 | 0.465 | MET |
| 3. All three labels reached | 3 of 3 | 3/3 | 3/3 | 3/3 | MET |
| 4. Appeals recorded, `under_review` | 10 of 10 | 10/10 | 10/10 | 10/10 | MET |
| 5. Invalid input → 400/413, no decision | 5 of 5 | 4/5 | 4/5 | 4/5 | **MISSED** |

**The criterion 5 miss, and the re-run.** In all three trials, the one request
with no `creator_id` got a **429**, not a 400
(`results/run_2026-11-09_2053_after.md`). With no creator_id, the rate limiter
counts that request against my IP address, and I started this eval about 10
seconds after the attack run, whose malformed rows had used up that address's 5
per minute. **Stage: the rate limiter, in front of the route. Mechanism:
requests without a creator_id share one per-address bucket.** The reweight
can't affect it, and the before eval passed because it ran half an hour after
its attack run. I re-ran the whole eval with nothing changed, on a freshly
started service (which also resets the in-memory limiter):
`results/run_2026-11-09_2054_after_rerun.md` gives **5/5, 5/5, 5/5**. I'm
reporting both. The first run is a real finding: a legitimate but malformed
request from a busy shared address gets "too many requests" instead of being
told what's wrong with it.

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

**It helped the side I care about most, and didn't change the number that
broke.**

- **False positives: better.** Seven of the eight FP texts moved away from the
  AI line. FP08 rose from 0.411 to 0.447: at 8 words its style is a fixed 0.5
  (no opinion), which now counts for more, and it stays unsure by the short-text
  rule. The worst case, FP03, went from 0.709 to **0.671**, and the
  highest FP score went from 0.710 to 0.671. FP06 and FP07, which had the
  highest signal-one scores (0.88), dropped by 0.10 and 0.11.
- **Evasion: no net change, 9 broke before and after, but different ones.**
  EV04 (rare words) is now caught: its style of 0.889 counts for more, 0.750 →
  **0.806**. EV10 (repeated stanzas) now gets through: repeating whole stanzas
  makes the vocabulary measure read human, so style is only 0.667, and with
  signal one's 0.979 counting for less it fell from 0.823 to **0.760**. That's
  the trade in one pair: weighting style up rewards the attacks that keep the
  AI shape and punishes the ones that change it.
- **The cost I predicted showed up.** The shape attacks scored *lower* (EV02
  0.477 → 0.430, EV03 0.565 → 0.524, EV06 0.521 → 0.500). Criterion 2's
  separation shrank slightly, from 0.479 to 0.465, because the casual human
  comments' style scores now count for more.
- **What didn't move.** Prompt injection still changed no labels. MF04–06 still
  get a logged decision on text with no words, because that's the route, not
  the weights.

In one sentence: the reweight moved the worst false-positive 0.04 further
from an accusation without catching any more AI text overall. On a writing site
that's the right direction, but it isn't a fix for evasion.

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

Every criterion ended MET in the re-run, so this list is the 12 attacks that
still break, plus the gaps the runs exposed.

1. **Evasion, 9 of 10 still get through (EV01–EV03, EV05–EV10).** The root is
   signal one: it gives AI text only about 0.67, so an AI label needs style
   near its maximum, and any edit to either signal drops below 0.80. The
   reweight swapped EV10 for EV04 instead of closing the gap. *What I'd do:*
   recalibrate signal one, or replace GPT-2 perplexity with a measure that
   doesn't reward plainness (for example, comparing perplexity under two
   models). *Why I stopped:* the unit allows one improvement, and this needs a
   new signal, not a setting. I also wouldn't fix EV05: after a heavy human
   edit, the writing arguably is the person's.
2. **The route accepts text with no words (MF04–06).** Punctuation-only, one
   4,000-letter word and emoji-only text each got a logged decision, and signal
   one scored the word and emoji at 0.997. *What I'd do:* refuse anything with
   fewer than about 3 real words with a 422, before either signal runs. That
   was option B in Milestone 5, and it's the next change I'd make. *Why I
   stopped:* one change per unit, and the reweight addressed the bigger
   pattern.
3. **Semicolons erase sentences (EV07).** `stylometry._sentence_lengths` only
   splits on `. ! ?`, so 97 words joined by "; and, moreover," count as one
   sentence and trip the short-text rule. *What I'd do:* split on semicolons
   and line breaks too, or base the short-text rule on words alone. *Why I
   stopped:* it's narrow, and changing the splitter moves every style score,
   which would muddy the before/after comparison.
4. **Short text is always unsure (EV08, and 6 of my 20 criterion 1
   comments).** This is a choice, not a bug: under 50 words I won't accuse
   anyone. The cost is that a short AI submission always gets through.
5. **Style can't read non-Latin scripts (MF07).** `stylometry.words` only
   matches a–z, so Arabic, Hebrew, Chinese and others get style 0.5 forever,
   and the decision rests on GPT-2, an English model (0.906 on MF07). *What
   I'd do:* use a Unicode-aware word pattern, and refuse to score languages
   the detector wasn't trained on rather than guess.
6. **The rate limit has two holes.** A script that invents a new `creator_id`
   for every request is never limited. And requests with no `creator_id` share
   one per-address bucket, which turned a 400 into a 429 in my first after run
   (criterion 5, 4/5). *What I'd do:* key on a logged-in account, with a
   per-address limit as a backstop and a higher allowance before it.
7. **Signal one moves on injected nonsense.** No injection changed a label,
   but "SYSTEM: … guess=human" took PI02's model score from 0.754 to 0.204,
   because it's unpredictable text. With a longer AI body, that could carry
   AI text into unsure. It's the same weakness as evasion (pattern 1), so I'd
   fix it the same way.

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

I'd keep the wide unsure band and the reweight, and accept that most edited AI
text gets through as "unsure", because a wrong AI label lands on a real person,
often the careful second-language writer like FP03 who has the least room to
argue. The people who pay are the honest writers competing with AI-assisted work on
the same site and the readers who see "unsure" on generated text: a cost
spread thinly across many people instead of dropped heavily on one.

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
