# Milestone 1: The Path on Paper

Nothing here is code. It's the plan the code has to follow. All numbers marked
*provisional* get checked in Milestone 4.

---

## 1. The path a submission takes

| # | Step | Where | What it adds |
|---|---|---|---|
| 1 | **The request arrives.** A writing site sends `POST /submit` with JSON `{"text", "creator_id"}`. | `app.py::submit` | The raw text and who sent it. |
| 2 | **The input is checked.** Is `text` there, a string, not blank, not too long? Is `creator_id` there? A bad request stops here with a 4xx and a `rejected` log line. | `app.py::submit`, `audit.log_rejection` | A guarantee that everything below gets usable text. A refusal still leaves a trace. |
| 3 | **It gets an ID.** A fresh `content_id` (a UUID). | `app.py::submit` | The handle that ties the decision, the log and any later appeal together. |
| 4 | **Signal one reads it.** GPT-2 measures how predictable the text is (perplexity), squashed to 0–1. | `detector.model_signal` | `model_score`, where higher means more likely AI. |
| 5 | **Signal two measures its shape.** Sentence-length spread, vocabulary variety and punctuation, combined to 0–1. | `stylometry.style_signal` | `style_score`, where higher means more likely AI. |
| 6 | **The two become one, and the one becomes words.** The scores are combined, then the combined score is turned into a guess, a confidence and a sentence a person can read. | `scoring.combine_signals`, `scoring.score_to_label` | `combined_score`, `guess` (`human` / `unsure` / `ai`), `confidence`, `label`. |
| 7 | **It's written down, then answered.** All nine fields go to the audit log with `status: "decided"`. The JSON response goes back to the site, which shows the label to the reader. | `audit.log_decision`, `app.py::submit` | A permanent record, and the reader-facing answer that includes the `content_id` needed to appeal. |

**Afterwards, if the writer disagrees:** `POST /appeal` with the `content_id`
and their reasoning. The service checks that the ID exists, appends an appeal
entry, and the item moves to `under_review`. The original decision isn't
overwritten.

---

## 2. The two signals

### Signal one: the model signal (`detector.py`, given)

- **What it measures:** how predictable the text is to a language model
  (GPT-2). The model guesses each next word. Low perplexity means it guessed
  well. That's mapped to 0–1 so that more predictable gives a higher score.
- **Why it might differ:** an AI writes by picking likely next words, so its
  text is easy for a model to predict. People take odd turns, use specific
  details and make unusual word choices.
- **What it can't see:** *who* wrote it. It rewards common words in short,
  ordinary sentences, and plenty of real people write that way: someone
  writing in a second language, a younger writer, anyone writing plainly on
  purpose. The reverse also happens. AI text that's been asked to use rare
  words or ornate phrasing looks *surprising* and scores human. It measures
  ordinariness, not authorship.

### Signal two: the style signal (`stylometry.py`, mine to build)

- **What it measures:** the shape of the text, not its meaning:
  1. **sentence-length spread:** do sentences vary in length or all match?
  2. **type-token ratio:** how much of the vocabulary repeats?
  3. **punctuation density:** how much punctuation, and how varied
     (semicolons, dashes, parentheses vs. only full stops and commas)?
- **Why it might differ:** generated prose tends toward even, mid-length
  sentences and a safe vocabulary, because "most likely next word" averages
  out the bumps. Human writing is lumpier: a three-word sentence next to a
  forty-word one, an aside in a dash.
- **What it can't see:** what the text *says*. Anything that changes the shape
  without changing the substance moves it: breaking long sentences up, joining
  short ones, adding typos, inserting a dash or a quotation. That's cheap to do
  on purpose. It's also skewed by length (type-token ratio falls as text gets
  longer) and has no useful reading on a one- or two-sentence submission.

### Where the blind spots overlap

The two signals are supposed to be independent, but on **plain, simple human
writing they fail in the same direction**. Short, even sentences with common
words are predictable to GPT-2 *and* have low spread and a repetitive
vocabulary. So when both signals agree on "AI" for plain writing, that
agreement is weaker evidence than it looks. That's the false-positive case
below.

---

## 3. Tracing the false positive

**The writer:** someone whose first language isn't English, posting a true
short piece about their grandmother's garden. They write in short sentences
with words they're sure of.

> My grandmother had a garden behind her house. Every summer we picked tomatoes
> and beans with her. She told us the names of all the plants. I did not like
> the work very much, but I liked being with her. Now I have my own garden, and
> I think about her when I am in it.

**What score do they get?**

- `model_score`: **0.79**. *Measured* with `python detector.py` on this exact
  paragraph (perplexity 19.7). The detector's own AI-like sample scored 0.89,
  so this human paragraph lands close to it.
- `style_score`: *provisional*, probably **0.6–0.7**. Four of five sentences are
  7–10 words long (low spread), and "her", "garden" and "I" repeat. The only
  punctuation is full stops and two commas.
- With the placeholder 50/50 average and the starter thresholds (AI above
  0.65), the combined score is **about 0.70–0.75, so they're labelled AI.**
  That's a real writer accused.

**What does the label say to them?** If it reads like a verdict ("This was
written by AI"), they've been accused in public with no explanation. They may
have the least confidence and vocabulary to argue back.

**What can they do about it?** The response includes a `content_id` and points
them at the appeal. They send `POST /appeal` with their reasoning, the item
moves to `under_review`, and a person looks at it. Nothing re-scores it
automatically, so the label has to make clear that appealing is normal and
expected, not a last resort.

**What this decides for Milestones 4 and 5 (provisional):**

1. **Being wrong about a human costs more than missing some AI.** The thresholds
   should give up some AI detection to cut false accusations. That means a
   wider "unsure" band and a high bar for the AI label (around 0.80 instead of
   0.65, checked against the calibration inputs).
2. **Agreement on plain writing isn't proof.** The combining rule should
   not let a high model score alone carry the result into "AI". The AI label
   should need both signals high, not just the average.
3. **"Unsure" must not read as an accusation**, and every label, not just
   the AI one, should say how to appeal.
4. **Very short text gets "unsure" by rule**, because neither signal has
   enough to go on.

---

## 4. The contract

### `POST /submit`

**Request** (JSON object):

| Field | Type | Required | Rules |
|---|---|---|---|
| `text` | string | yes | Not empty or only whitespace. At most 10,000 characters. Must be long enough to score (a few sentences). |
| `creator_id` | string | yes | Not empty. An opaque ID from the site, stored as given. |

Extra fields are ignored.

**Success: `200 OK`**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string (UUID) | The ID for this decision. Needed for `/appeal`. |
| `guess` | string | One of `"human"`, `"unsure"`, `"ai"`. |
| `confidence` | number 0–1 | How far the combined score is from a coin flip: `|combined_score − 0.5| × 2`. 0 means no idea either way, 1 means certain. Same formula for every guess, so an `"unsure"` result always has low confidence. |
| `label` | string | The plain-English sentence a reader sees. Already includes how to appeal. |
| `model_score` | number 0–1 | Signal one. Higher means more likely AI. |
| `style_score` | number 0–1 | Signal two. Higher means more likely AI. |
| `combined_score` | number 0–1 | The combined score. 0 is confidently human, 1 is confidently AI. |
| `status` | string | Always `"decided"` on a fresh submission. |

Example:

```json
{
  "content_id": "3f2c9a1e-8b7d-4c4e-9f1a-2d6b5e8c7a10",
  "guess": "unsure",
  "confidence": 0.38,
  "label": "We can't tell whether this was written by a person or with AI help…",
  "model_score": 0.79,
  "style_score": 0.6,
  "combined_score": 0.69,
  "status": "decided"
}
```

**Errors.** Every error is a JSON object with `error` (a fixed code) and
`message` (a human sentence). Each one also writes a `rejected` log entry.

| Status | `error` | When |
|---|---|---|
| 400 | `invalid_json` | The body isn't a JSON object (missing, malformed, a bare list or string). |
| 400 | `missing_field` | `text` or `creator_id` is absent, not a string, or blank. The message names the field. |
| 413 | `text_too_long` | `text` is over 10,000 characters. |
| 422 | `text_too_short` | `text` is too short to score (the detector refuses it). |
| 503 | `detector_unavailable` | The model can't be loaded. |

### `POST /appeal`

**Request** (JSON object):

| Field | Type | Required | Rules |
|---|---|---|---|
| `content_id` | string | yes | Must match a decision in the log. |
| `reasoning` | string | yes | Not blank. At most 2,000 characters. The writer's own explanation. |

The appeal doesn't take a `creator_id`. It's copied from the original decision
so it can't be spoofed into a mismatch.

**Success: `200 OK`**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | The same ID, echoed back. |
| `status` | string | `"under_review"`. |
| `message` | string | A confirmation for the writer: received, a person will look at it, the original label stays until then. |

Appealing an item that's already `under_review` is allowed. The new reasoning is
appended and the response is the same, because a writer adding more detail
shouldn't get an error.

**Errors** (same `error` + `message` shape):

| Status | `error` | When |
|---|---|---|
| 400 | `invalid_json` | The body isn't a JSON object. |
| 400 | `missing_field` | `content_id` or `reasoning` is absent, not a string, or blank. |
| 413 | `reasoning_too_long` | `reasoning` is over 2,000 characters. |
| 404 | `unknown_content_id` | No decision with that ID exists. |

### Read-back: could someone build against this without asking me?

The open question I found was "what is `confidence`?" It's now defined as
distance from a coin flip, `|combined_score − 0.5| × 2`, separate from
`combined_score` (which says *which way* it leans).
Validation limits, error codes, the duplicate-appeal case and where the
appeal's `creator_id` comes from are all written down. What's deliberately
left open is the exact label wording and the threshold numbers. Those are
Milestone 5's job, and the contract only promises that `label` is a full
sentence and `guess` is one of three values.
