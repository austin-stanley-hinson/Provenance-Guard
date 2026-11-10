# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 20:14
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `e6e18305-9bfa-4c42-ade0-c919acffd0c0` | unsure | 0.123 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `18cd1d9a-e898-4495-83b0-e2b7cfde8a33` | unsure | 0.046 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `af2f7c18-5358-485b-8ca4-0c9ea506988c` | unsure | 0.130 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `d10e04fd-9a0d-4dea-be07-06b3f11e4e43` | unsure | 0.501 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `db4016f5-7a6e-41fe-8d32-c737dc5b6fcb` | unsure | 0.372 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `9e1bd83c-5def-4f43-a623-fb9f88e5700c` | unsure | 0.042 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `e614c7dd-e27b-49fa-8d67-739c18df4f6e` | unsure | 0.086 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `be64e7a0-4391-40bf-9ebb-36a411e80948` | unsure | 0.255 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `bd9eec90-215e-4c50-9c51-5577e6af59bd` | unsure | 0.239 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `01c537d5-9186-44dc-9b45-4bfc95829d44` | ai | 0.646 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `d77355ef-f148-4717-ba46-59c50d3c457a` | unsure | 0.087 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `916c9347-0059-4d1e-9b9e-c58a1f44a875` | unsure | 0.372 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `2c85a210-d45a-4b7a-8bbb-24d12b5a0744` | unsure | 0.419 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `40231249-942e-4b6d-9cc0-2d8e7da362df` | unsure | 0.419 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `f1c49b6d-06a8-45a5-8fb7-89710ef38405` | unsure | 0.403 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `2e3f4373-aa3a-49d4-b866-7469e7795025` | unsure | 0.282 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `40937006-9c80-4b9f-a9b7-e31839f155e0` | unsure | 0.215 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `4d387547-7c74-4dc4-9a53-77fb787afdba` | unsure | 0.178 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `25b43860-d203-4fa7-a600-3aa3f5662cd9` | unsure | 0.037 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `6d95189b-210a-4ae2-92a3-e59ff3e96c02` | unsure | 0.296 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `beae16d0-c47d-4e7c-89da-ada3bb2454ae` | unsure | 0.029 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `b2a05ca7-d97c-4af2-aa4b-fe24ef23599f` | unsure | 0.164 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `7bdbb96b-c7c3-47d7-836e-decd790672cc` | unsure | 0.140 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `797660cb-cd15-48a2-b0e0-49d41c27c95c` | unsure | 0.055 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 422 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `1159fdd6-7eb2-4e7f-bec6-aea8aa93aea4` | unsure | 0.500 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `446d5995-7f34-40b2-a7ab-d47ed1df38d2` | unsure | 0.489 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `1fcd670b-9cef-494d-a214-f8296d6f1501` | unsure | 0.498 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `8521a7f6-e58a-4334-b031-cf16f8e31b62` | unsure | 0.497 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `e9fef754-3545-49a5-b1ca-73806b91cf23` | unsure | 0.406 | HELD |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `397dfb19-738d-4f0e-ace2-72b3037663ab` | unsure | 0.471 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d4d09449-647b-4901-91c2-178e24e6811f` | unsure | 0.471 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `adecb073-35d0-4079-8eec-7c3e71eabecc` | unsure | 0.471 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6aa963e3-23c3-4c15-af8b-1246939b72bc` | unsure | 0.471 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `edf61b77-efe0-4dc0-99b6-bba29533cdb6` | unsure | 0.471 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "e6e18305-9bfa-4c42-ade0-c919acffd0c0",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.1226,
  "model_score": 0.1635,
  "style_score": 0.959,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "18cd1d9a-e898-4495-83b0-e2b7cfde8a33",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.0464,
  "model_score": 0.5943,
  "style_score": 0.3592,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "af2f7c18-5358-485b-8ca4-0c9ea506988c",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.13,
  "model_score": 0.6662,
  "style_score": 0.4638,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "d10e04fd-9a0d-4dea-be07-06b3f11e4e43",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5008,
  "model_score": 0.6114,
  "style_score": 0.8894,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "db4016f5-7a6e-41fe-8d32-c737dc5b6fcb",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.372,
  "model_score": 0.3212,
  "style_score": 0.3069,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "9e1bd83c-5def-4f43-a623-fb9f88e5700c",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.0416,
  "model_score": 0.5727,
  "style_score": 0.4689,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "e614c7dd-e27b-49fa-8d67-739c18df4f6e",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.0862,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "be64e7a0-4391-40bf-9ebb-36a411e80948",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.2548,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "bd9eec90-215e-4c50-9c51-5577e6af59bd",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.2386,
  "model_score": 0.7042,
  "style_score": 0.5344,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "01c537d5-9186-44dc-9b45-4bfc95829d44",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.6458,
  "model_score": 0.9792,
  "style_score": 0.6667,
  "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "d77355ef-f148-4717-ba46-59c50d3c457a",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.087,
  "model_score": 0.6175,
  "style_score": 0.4696,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "916c9347-0059-4d1e-9b9e-c58a1f44a875",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.3718,
  "model_score": 0.7387,
  "style_score": 0.6331,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "2c85a210-d45a-4b7a-8bbb-24d12b5a0744",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.4188,
  "model_score": 0.8051,
  "style_score": 0.6137,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "40231249-942e-4b6d-9cc0-2d8e7da362df",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.4194,
  "model_score": 0.8329,
  "style_score": 0.5864,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "f1c49b6d-06a8-45a5-8fb7-89710ef38405",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.4032,
  "model_score": 0.8005,
  "style_score": 0.6026,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "2e3f4373-aa3a-49d4-b866-7469e7795025",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.2822,
  "model_score": 0.8814,
  "style_score": 0.4007,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "40937006-9c80-4b9f-a9b7-e31839f155e0",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.215,
  "model_score": 0.8816,
  "style_score": 0.3333,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "4d387547-7c74-4dc4-9a53-77fb787afdba",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.1776,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "25b43860-d203-4fa7-a600-3aa3f5662cd9",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.0374,
  "model_score": 0.4625,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "6d95189b-210a-4ae2-92a3-e59ff3e96c02",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.2956,
  "model_score": 0.2044,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "beae16d0-c47d-4e7c-89da-ada3bb2454ae",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.0288,
  "model_score": 0.5943,
  "style_score": 0.4345,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "b2a05ca7-d97c-4af2-aa4b-fe24ef23599f",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.164,
  "model_score": 0.4998,
  "style_score": 0.3361,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "7bdbb96b-c7c3-47d7-836e-decd790672cc",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.14,
  "model_score": 0.6401,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "797660cb-cd15-48a2-b0e0-49d41c27c95c",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.0552,
  "model_score": 0.5583,
  "style_score": 0.4969,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "1159fdd6-7eb2-4e7f-bec6-aea8aa93aea4",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "446d5995-7f34-40b2-a7ab-d47ed1df38d2",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.4888,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "1fcd670b-9cef-494d-a214-f8296d6f1501",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.4976,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "8521a7f6-e58a-4334-b031-cf16f8e31b62",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.497,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "e9fef754-3545-49a5-b1ca-73806b91cf23",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.4064,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "397dfb19-738d-4f0e-ace2-72b3037663ab",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4714,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "d4d09449-647b-4901-91c2-178e24e6811f",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4714,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "adecb073-35d0-4079-8eec-7c3e71eabecc",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4714,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "6aa963e3-23c3-4c15-af8b-1246939b72bc",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4714,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "edf61b77-efe0-4dc0-99b6-bba29533cdb6",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4714,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
