# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False Positive Rate

Out of 20 samples of verified human-written text, no more than 1 (5%) should receive a high-confidence AI label.

**Why this target:** Falsely accusing someone of using AI could damage their credibility. I'd rather have the system return "unsure" than confidently make the wrong accusation.

---

## 2. Confidence Score Separation

Across a test set of 10 human-written and 10 AI-generated samples, the average AI-likelihood score for AI-generated text should be at least 0.25 higher than the average score for human-written text.

**Why this target:** The two signals should produce meaningful differences between writing samples rather than returning similar scores for everything. A 0.25 gap gives me a measurable target without expecting perfect detection.

---

## 3. Label Coverage and Thresholds

Every valid combined score between 0 and 1 (0 = confidently human, 1 = confidently AI) must map to exactly one of three labels:

- **0.00–0.20:** High-confidence human
- **Above 0.20 and below 0.80:** Unsure
- **0.80–1.00:** High-confidence AI

All three labels must be reachable through testing, with no scores left unclassified.

**Why this target:** I'm deliberately keeping the unsure range wide because the consequences of a false accusation are greater than those of missing AI-generated content. The system should only make strong claims when the score is sufficiently convincing.

---

## 4. Appeal Handling

For 10 valid appeals submitted through `POST /appeal`, all 10 must be recorded with their `content_id` and reasoning, update the corresponding content status to `under_review`, and return a confirmation response.

**Why this target:** Writers should have a reliable way to challenge a classification. An appeal should never silently disappear, especially when someone's work has been incorrectly flagged.

---

## 5. Invalid Input Handling

The `POST /submit` endpoint must reject 100% of tested invalid requests, including missing `text`, empty or whitespace-only text, missing `creator_id`, and text exceeding 10,000 characters. Each must return HTTP 400 or 413 with a clear JSON error message, without crashing the service or creating a decision or classification for it (a `rejected` entry in the audit log is expected).

**Why this target:** Bad inputs shouldn't break the service or produce misleading classifications. A defined text limit also prevents excessively large submissions from consuming unnecessary processing resources.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
