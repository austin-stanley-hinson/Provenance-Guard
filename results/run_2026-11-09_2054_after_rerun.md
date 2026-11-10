# Run log — after_rerun

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-09 20:54

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. c1 human writing, unseen |  |   |   |   |  |
| 2. c2 human half |  |   |   |   |  |
| 2. c2 AI half |  |   |   |   |  |
| 3. c3 label coverage |  |   |   |   |  |
| 5. c5 invalid input |  |   |   |   |  |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### c1 human writing, unseen

**Trial 1**

```json
[
  {
    "status": 200,
    "content_id": "332ab103-b32f-46c6-b74a-1c40105df5af",
    "guess": "human",
    "combined_score": 0.1745,
    "confidence": 0.651,
    "model_score": 0.25,
    "style_score": 0.1422,
    "label": "This looks like it was written by a person. If you think we got that wrong, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "\"For reference, I am an international student (so according to this su"
  },
  {
    "status": 200,
    "content_id": "184ae4e4-0fd4-4b1b-892f-91a6a353586f",
    "guess": "human",
    "combined_score": 0.0818,
    "confidence": 0.8364,
    "model_score": 0.257,
    "style_score": 0.0067,
    "label": "This looks like it was written by a person. If you think we got that wrong, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "truly an excellent find lol, some of my other favorite moments:\n \"We a"
  },
  {
    "status": 200,
    "content_id": "43e5c909-cc11-4380-a6ce-c7e41e318ba4",
    "guess": "unsure",
    "combined_score": 0.4231,
    "confidence": 0.1538,
    "model_score": 0.2438,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "This hurts hard as a Canadian, everyone and their mother watches Ameri"
  },
  {
    "status": 200,
    "content_id": "3b3d599c-0dcb-4b48-9c65-015088d9c67e",
    "guess": "unsure",
    "combined_score": 0.423,
    "confidence": 0.154,
    "model_score": 0.2434,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "It was still cuastic before the pandemic. Internships were unpaid, peo"
  },
  {
    "status": 200,
    "content_id": "6b9aa8ec-f982-4659-bbdd-a73a937832f0",
    "guess": "unsure",
    "combined_score": 0.4154,
    "confidence": 0.1692,
    "model_score": 0.218,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Just curious, but let\u2019s say we have an agent that we provide skills to"
  },
  {
    "status": 200,
    "content_id": "a8e59172-f7e9-4715-8472-427919b09fb2",
    "guess": "unsure",
    "combined_score": 0.4882,
    "confidence": 0.0236,
    "model_score": 0.4235,
    "style_score": 0.5159,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I mean yeah I agree that spending thousands on degree to make a fracti"
  },
  {
    "status": 200,
    "content_id": "2ae82e58-614e-4986-a4c3-26bb36f36fe0",
    "guess": "unsure",
    "combined_score": 0.584,
    "confidence": 0.168,
    "model_score": 0.3137,
    "style_score": 0.6999,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "This is where the industry is headed, even in HCOL areas. Similar prof"
  },
  {
    "status": 200,
    "content_id": "182ccc93-fcd5-4a67-8818-2603732923ce",
    "guess": "unsure",
    "combined_score": 0.4397,
    "confidence": 0.1206,
    "model_score": 0.3099,
    "style_score": 0.4954,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Imagine expecting a neurosurgeon to be able to explain how to perform "
  },
  {
    "status": 200,
    "content_id": "1401c4ea-4620-4da6-84d7-9b7f7937beb6",
    "guess": "unsure",
    "combined_score": 0.413,
    "confidence": 0.174,
    "model_score": 0.2101,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "To add to this, poor performance on exams is now immediately associate"
  },
  {
    "status": 200,
    "content_id": "a2f63fd2-b169-409e-9d6a-d1446838e12c",
    "guess": "unsure",
    "combined_score": 0.3601,
    "confidence": 0.2798,
    "model_score": 0.2925,
    "style_score": 0.3891,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "This 100 percent. It's either doom and gloom or \"hey look how great my"
  },
  {
    "status": 200,
    "content_id": "59724224-0b05-43d1-97e2-04e5489ef416",
    "guess": "unsure",
    "combined_score": 0.4644,
    "confidence": 0.0712,
    "model_score": 0.3815,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Coming from someone who has been in both sides of the table: if you ca"
  },
  {
    "status": 200,
    "content_id": "a0e1dbc3-1ac9-46a1-93f8-49a9efb9b131",
    "guess": "unsure",
    "combined_score": 0.3629,
    "confidence": 0.2742,
    "model_score": 0.4895,
    "style_score": 0.3086,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Don't have a full time job yet, but I do a lot of contracts for AI com"
  },
  {
    "status": 200,
    "content_id": "174fc984-6c0d-443b-89d7-06bf47567f49",
    "guess": "unsure",
    "combined_score": 0.5333,
    "confidence": 0.0666,
    "model_score": 0.611,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "exactly, people can be very smart and capable but sometimes things jus"
  },
  {
    "status": 200,
    "content_id": "9b226ed1-f289-482c-bd35-fad0a5b24f8e",
    "guess": "unsure",
    "combined_score": 0.3883,
    "confidence": 0.2234,
    "model_score": 0.7334,
    "style_score": 0.2404,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "That might or might not happen. And even if it does happen, OP will ha"
  },
  {
    "status": 200,
    "content_id": "b0db35a5-09f4-4c57-8d0e-55fe8949d0a5",
    "guess": "unsure",
    "combined_score": 0.21,
    "confidence": 0.58,
    "model_score": 0.4469,
    "style_score": 0.0147,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "My comment was regarding internship. For full time if you quit, Google"
  },
  {
    "status": 200,
    "content_id": "6d99423d-71f8-4dd5-8215-32f87c372eba",
    "guess": "unsure",
    "combined_score": 0.7335,
    "confidence": 0.467,
    "model_score": 0.4697,
    "style_score": 0.8465,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "yep i worked in software for a retail company as my first tech job. su"
  },
  {
    "status": 200,
    "content_id": "a1a01e3c-70f8-40d3-b7ee-73d20f982575",
    "guess": "unsure",
    "combined_score": 0.2265,
    "confidence": 0.547,
    "model_score": 0.4523,
    "style_score": 0.1297,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I agree with basically everything you said in essence, but saying \"I g"
  },
  {
    "status": 200,
    "content_id": "e7b82590-e1f0-4b2e-8ab2-093f9fa58d1b",
    "guess": "unsure",
    "combined_score": 0.5101,
    "confidence": 0.0202,
    "model_score": 0.2721,
    "style_score": 0.6121,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "21yrs ago none of my fellow students were complaining, as far as I rem"
  },
  {
    "status": 200,
    "content_id": "80c89383-be35-4a2d-8f8a-9a03bb115a52",
    "guess": "unsure",
    "combined_score": 0.362,
    "confidence": 0.276,
    "model_score": 0.3181,
    "style_score": 0.3808,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "do you have any tips on how to find hackathons like that where its all"
  },
  {
    "status": 200,
    "content_id": "1a767f89-786e-4eb8-8d2a-57624b6a2368",
    "guess": "unsure",
    "combined_score": 0.275,
    "confidence": 0.45,
    "model_score": 0.2632,
    "style_score": 0.2801,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I just skip the interview if they ask leet code, or take home test or "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "content_id": "2340b302-7ce3-4f89-a511-9c4ca9c98f3a",
    "guess": "human",
    "combined_score": 0.1745,
    "confidence": 0.651,
    "model_score": 0.25,
    "style_score": 0.1422,
    "label": "This looks like it was written by a person. If you think we got that wrong, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "\"For reference, I am an international student (so according to this su"
  },
  {
    "status": 200,
    "content_id": "99a36734-b1de-4d51-adb3-8716f608f1b1",
    "guess": "human",
    "combined_score": 0.0818,
    "confidence": 0.8364,
    "model_score": 0.257,
    "style_score": 0.0067,
    "label": "This looks like it was written by a person. If you think we got that wrong, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "truly an excellent find lol, some of my other favorite moments:\n \"We a"
  },
  {
    "status": 200,
    "content_id": "053185ff-2b75-45c5-a735-8cd33d351f15",
    "guess": "unsure",
    "combined_score": 0.4231,
    "confidence": 0.1538,
    "model_score": 0.2438,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "This hurts hard as a Canadian, everyone and their mother watches Ameri"
  },
  {
    "status": 200,
    "content_id": "726a8229-34a0-4de2-9b36-725ae137ee84",
    "guess": "unsure",
    "combined_score": 0.423,
    "confidence": 0.154,
    "model_score": 0.2434,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "It was still cuastic before the pandemic. Internships were unpaid, peo"
  },
  {
    "status": 200,
    "content_id": "f07a343d-3ab0-454d-9554-ff43e72dc483",
    "guess": "unsure",
    "combined_score": 0.4154,
    "confidence": 0.1692,
    "model_score": 0.218,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Just curious, but let\u2019s say we have an agent that we provide skills to"
  },
  {
    "status": 200,
    "content_id": "b7f8f1a6-650e-404b-8119-0584d08b4dc8",
    "guess": "unsure",
    "combined_score": 0.4882,
    "confidence": 0.0236,
    "model_score": 0.4235,
    "style_score": 0.5159,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I mean yeah I agree that spending thousands on degree to make a fracti"
  },
  {
    "status": 200,
    "content_id": "70436fed-9a4e-4171-8b1d-874a89f6fe14",
    "guess": "unsure",
    "combined_score": 0.584,
    "confidence": 0.168,
    "model_score": 0.3137,
    "style_score": 0.6999,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "This is where the industry is headed, even in HCOL areas. Similar prof"
  },
  {
    "status": 200,
    "content_id": "31386239-3f00-4d16-b968-83faa52e56cc",
    "guess": "unsure",
    "combined_score": 0.4397,
    "confidence": 0.1206,
    "model_score": 0.3099,
    "style_score": 0.4954,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Imagine expecting a neurosurgeon to be able to explain how to perform "
  },
  {
    "status": 200,
    "content_id": "0b7989ce-edcf-4ae0-ac70-9e4122ababf3",
    "guess": "unsure",
    "combined_score": 0.413,
    "confidence": 0.174,
    "model_score": 0.2101,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "To add to this, poor performance on exams is now immediately associate"
  },
  {
    "status": 200,
    "content_id": "a2afc62a-4d40-458b-af86-e2907ae932bf",
    "guess": "unsure",
    "combined_score": 0.3601,
    "confidence": 0.2798,
    "model_score": 0.2925,
    "style_score": 0.3891,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "This 100 percent. It's either doom and gloom or \"hey look how great my"
  },
  {
    "status": 200,
    "content_id": "1b836dcc-b0d2-4a95-9dee-543bf004694d",
    "guess": "unsure",
    "combined_score": 0.4644,
    "confidence": 0.0712,
    "model_score": 0.3815,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Coming from someone who has been in both sides of the table: if you ca"
  },
  {
    "status": 200,
    "content_id": "2ab2b689-7004-4378-bd5b-27938a32b5ca",
    "guess": "unsure",
    "combined_score": 0.3629,
    "confidence": 0.2742,
    "model_score": 0.4895,
    "style_score": 0.3086,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Don't have a full time job yet, but I do a lot of contracts for AI com"
  },
  {
    "status": 200,
    "content_id": "93fbbb8d-a75e-4402-adbd-3f6cb912690f",
    "guess": "unsure",
    "combined_score": 0.5333,
    "confidence": 0.0666,
    "model_score": 0.611,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "exactly, people can be very smart and capable but sometimes things jus"
  },
  {
    "status": 200,
    "content_id": "42938f8a-d3be-46de-aa2e-4db5c27a75b9",
    "guess": "unsure",
    "combined_score": 0.3883,
    "confidence": 0.2234,
    "model_score": 0.7334,
    "style_score": 0.2404,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "That might or might not happen. And even if it does happen, OP will ha"
  },
  {
    "status": 200,
    "content_id": "7d79aa47-591a-4df0-a3da-6fb31927c5ad",
    "guess": "unsure",
    "combined_score": 0.21,
    "confidence": 0.58,
    "model_score": 0.4469,
    "style_score": 0.0147,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "My comment was regarding internship. For full time if you quit, Google"
  },
  {
    "status": 200,
    "content_id": "ab10c8bd-364e-436e-9cf9-cbf63ef9d5c2",
    "guess": "unsure",
    "combined_score": 0.7335,
    "confidence": 0.467,
    "model_score": 0.4697,
    "style_score": 0.8465,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "yep i worked in software for a retail company as my first tech job. su"
  },
  {
    "status": 200,
    "content_id": "6d26afc8-9a28-4067-baca-95706600c669",
    "guess": "unsure",
    "combined_score": 0.2265,
    "confidence": 0.547,
    "model_score": 0.4523,
    "style_score": 0.1297,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I agree with basically everything you said in essence, but saying \"I g"
  },
  {
    "status": 200,
    "content_id": "9a315a07-f36d-4e03-be78-a392e6e4d3a7",
    "guess": "unsure",
    "combined_score": 0.5101,
    "confidence": 0.0202,
    "model_score": 0.2721,
    "style_score": 0.6121,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "21yrs ago none of my fellow students were complaining, as far as I rem"
  },
  {
    "status": 200,
    "content_id": "7de382a4-a5da-4004-8478-8df1d197753e",
    "guess": "unsure",
    "combined_score": 0.362,
    "confidence": 0.276,
    "model_score": 0.3181,
    "style_score": 0.3808,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "do you have any tips on how to find hackathons like that where its all"
  },
  {
    "status": 200,
    "content_id": "68aa07d4-eeb8-4a47-a629-f717dbc14343",
    "guess": "unsure",
    "combined_score": 0.275,
    "confidence": 0.45,
    "model_score": 0.2632,
    "style_score": 0.2801,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I just skip the interview if they ask leet code, or take home test or "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "content_id": "a57ff348-9625-4e5f-895d-ec6f7e399dda",
    "guess": "human",
    "combined_score": 0.1745,
    "confidence": 0.651,
    "model_score": 0.25,
    "style_score": 0.1422,
    "label": "This looks like it was written by a person. If you think we got that wrong, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "\"For reference, I am an international student (so according to this su"
  },
  {
    "status": 200,
    "content_id": "59444464-8e62-480f-8975-522040129c16",
    "guess": "human",
    "combined_score": 0.0818,
    "confidence": 0.8364,
    "model_score": 0.257,
    "style_score": 0.0067,
    "label": "This looks like it was written by a person. If you think we got that wrong, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "truly an excellent find lol, some of my other favorite moments:\n \"We a"
  },
  {
    "status": 200,
    "content_id": "2be9795c-a49c-4da0-9a7d-7edd975b464a",
    "guess": "unsure",
    "combined_score": 0.4231,
    "confidence": 0.1538,
    "model_score": 0.2438,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "This hurts hard as a Canadian, everyone and their mother watches Ameri"
  },
  {
    "status": 200,
    "content_id": "3bf69727-a486-41ad-b8c3-46fd6d64844a",
    "guess": "unsure",
    "combined_score": 0.423,
    "confidence": 0.154,
    "model_score": 0.2434,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "It was still cuastic before the pandemic. Internships were unpaid, peo"
  },
  {
    "status": 200,
    "content_id": "9482db30-2396-43ab-8a9f-0f7793ba28dc",
    "guess": "unsure",
    "combined_score": 0.4154,
    "confidence": 0.1692,
    "model_score": 0.218,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Just curious, but let\u2019s say we have an agent that we provide skills to"
  },
  {
    "status": 200,
    "content_id": "afdc0156-b451-46e8-aeff-9cc3151b410d",
    "guess": "unsure",
    "combined_score": 0.4882,
    "confidence": 0.0236,
    "model_score": 0.4235,
    "style_score": 0.5159,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I mean yeah I agree that spending thousands on degree to make a fracti"
  },
  {
    "status": 200,
    "content_id": "4d81e2e5-71f6-4fb9-be88-f4680af0a509",
    "guess": "unsure",
    "combined_score": 0.584,
    "confidence": 0.168,
    "model_score": 0.3137,
    "style_score": 0.6999,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "This is where the industry is headed, even in HCOL areas. Similar prof"
  },
  {
    "status": 200,
    "content_id": "db28f323-651c-4620-b338-17e9502c3d37",
    "guess": "unsure",
    "combined_score": 0.4397,
    "confidence": 0.1206,
    "model_score": 0.3099,
    "style_score": 0.4954,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Imagine expecting a neurosurgeon to be able to explain how to perform "
  },
  {
    "status": 200,
    "content_id": "c27307d6-c74c-4e37-9ca9-571444f556c6",
    "guess": "unsure",
    "combined_score": 0.413,
    "confidence": 0.174,
    "model_score": 0.2101,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "To add to this, poor performance on exams is now immediately associate"
  },
  {
    "status": 200,
    "content_id": "0001f534-6707-493a-bdd6-931611d90171",
    "guess": "unsure",
    "combined_score": 0.3601,
    "confidence": 0.2798,
    "model_score": 0.2925,
    "style_score": 0.3891,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "This 100 percent. It's either doom and gloom or \"hey look how great my"
  },
  {
    "status": 200,
    "content_id": "a270c7ce-4af8-4595-b5eb-69829d4263a6",
    "guess": "unsure",
    "combined_score": 0.4644,
    "confidence": 0.0712,
    "model_score": 0.3815,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Coming from someone who has been in both sides of the table: if you ca"
  },
  {
    "status": 200,
    "content_id": "2ac1d78a-2122-457d-ba02-d65f82d208e4",
    "guess": "unsure",
    "combined_score": 0.3629,
    "confidence": 0.2742,
    "model_score": 0.4895,
    "style_score": 0.3086,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Don't have a full time job yet, but I do a lot of contracts for AI com"
  },
  {
    "status": 200,
    "content_id": "872a7ad5-314f-421e-87b7-130e0d118eec",
    "guess": "unsure",
    "combined_score": 0.5333,
    "confidence": 0.0666,
    "model_score": 0.611,
    "style_score": 0.5,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "exactly, people can be very smart and capable but sometimes things jus"
  },
  {
    "status": 200,
    "content_id": "6a04ff80-263a-4c85-a6a9-0760523e758e",
    "guess": "unsure",
    "combined_score": 0.3883,
    "confidence": 0.2234,
    "model_score": 0.7334,
    "style_score": 0.2404,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "That might or might not happen. And even if it does happen, OP will ha"
  },
  {
    "status": 200,
    "content_id": "a405373f-fcef-4039-a04b-1356b0efc3d5",
    "guess": "unsure",
    "combined_score": 0.21,
    "confidence": 0.58,
    "model_score": 0.4469,
    "style_score": 0.0147,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "My comment was regarding internship. For full time if you quit, Google"
  },
  {
    "status": 200,
    "content_id": "144c54d5-6ef7-46a1-b126-eef86878b19e",
    "guess": "unsure",
    "combined_score": 0.7335,
    "confidence": 0.467,
    "model_score": 0.4697,
    "style_score": 0.8465,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "yep i worked in software for a retail company as my first tech job. su"
  },
  {
    "status": 200,
    "content_id": "d78d06ed-74fe-4e65-bf12-9d88394e94d6",
    "guess": "unsure",
    "combined_score": 0.2265,
    "confidence": 0.547,
    "model_score": 0.4523,
    "style_score": 0.1297,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I agree with basically everything you said in essence, but saying \"I g"
  },
  {
    "status": 200,
    "content_id": "fb1526bb-f177-4746-8fc6-981c07696fb3",
    "guess": "unsure",
    "combined_score": 0.5101,
    "confidence": 0.0202,
    "model_score": 0.2721,
    "style_score": 0.6121,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "21yrs ago none of my fellow students were complaining, as far as I rem"
  },
  {
    "status": 200,
    "content_id": "e3d7d3e1-a634-4046-820a-46f000f4cd49",
    "guess": "unsure",
    "combined_score": 0.362,
    "confidence": 0.276,
    "model_score": 0.3181,
    "style_score": 0.3808,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "do you have any tips on how to find hackathons like that where its all"
  },
  {
    "status": 200,
    "content_id": "6fba91b1-4be6-45c6-b6fa-65eae5891dfc",
    "guess": "unsure",
    "combined_score": 0.275,
    "confidence": 0.45,
    "model_score": 0.2632,
    "style_score": 0.2801,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I just skip the interview if they ask leet code, or take home test or "
  }
]
```

### c2 human half

**Trial 1**

```json
[
  {
    "status": 200,
    "content_id": "fd0e10de-a2e5-4bc2-83c3-c7f52695f337",
    "guess": "unsure",
    "combined_score": 0.336,
    "confidence": 0.328,
    "model_score": 0.3423,
    "style_score": 0.3333,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I agree with this guy. Went to a career fair once and talked to a coup"
  },
  {
    "status": 200,
    "content_id": "c0b8abd8-53db-4e28-9dc2-7f3b0ec12357",
    "guess": "unsure",
    "combined_score": 0.3956,
    "confidence": 0.2088,
    "model_score": 0.3211,
    "style_score": 0.4276,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "While I generally agree with you, I'm calling cap on 240k\n There has t"
  },
  {
    "status": 200,
    "content_id": "35a24cdf-9d30-4d14-9ca5-b46d7ba2b618",
    "guess": "unsure",
    "combined_score": 0.4958,
    "confidence": 0.0084,
    "model_score": 0.0969,
    "style_score": 0.6667,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "You work for them \ud83d\ude22 . Trying to make it so commenter takes down post. "
  },
  {
    "status": 200,
    "content_id": "14bf7035-5ffc-484b-a3a1-500ea18c6047",
    "guess": "unsure",
    "combined_score": 0.4892,
    "confidence": 0.0216,
    "model_score": 0.4113,
    "style_score": 0.5226,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "can yall stop fantasizing about 10 years ago. if you joined the market"
  },
  {
    "status": 200,
    "content_id": "cbbaebac-2563-412b-9369-1640e7fc21a1",
    "guess": "human",
    "combined_score": 0.1364,
    "confidence": 0.7272,
    "model_score": 0.316,
    "style_score": 0.0594,
    "label": "This looks like it was written by a person. If you think we got that wrong, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I\u2019m not OP but the way I did it was a bit different: I\u2019d apply to regu"
  },
  {
    "status": 200,
    "content_id": "0a611db4-1dd4-4715-838d-ec08a093c9d4",
    "guess": "unsure",
    "combined_score": 0.3306,
    "confidence": 0.3388,
    "model_score": 0.3265,
    "style_score": 0.3324,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "stress isn\u2019t the only possibility for this to occur. There is a strong"
  },
  {
    "status": 200,
    "content_id": "a4bf786d-0839-4299-a846-c86670fc9448",
    "guess": "unsure",
    "combined_score": 0.2766,
    "confidence": 0.4468,
    "model_score": 0.1443,
    "style_score": 0.3333,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "There will be ppl in their 20s who complain one day this time is easy "
  },
  {
    "status": 200,
    "content_id": "8787347c-b672-4326-a549-8adefb2160ef",
    "guess": "unsure",
    "combined_score": 0.3296,
    "confidence": 0.3408,
    "model_score": 0.4078,
    "style_score": 0.2961,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I\u2019m sorry to hear that but it\u2019s like some people listen to their favor"
  },
  {
    "status": 200,
    "content_id": "bfc6c9dc-4e39-4eec-a305-2aac0334cbf1",
    "guess": "unsure",
    "combined_score": 0.4337,
    "confidence": 0.1326,
    "model_score": 0.1423,
    "style_score": 0.5586,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I am also under review. According to sources online for JPMC, under re"
  },
  {
    "status": 200,
    "content_id": "b65960f1-1176-480d-88ae-0346a769672a",
    "guess": "unsure",
    "combined_score": 0.4475,
    "confidence": 0.105,
    "model_score": 0.5415,
    "style_score": 0.4072,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Hey, I applied for a SWE role the questions for the virtual interview "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "content_id": "52b4dc24-9b71-4cf5-b674-80dbd2a2c44d",
    "guess": "unsure",
    "combined_score": 0.336,
    "confidence": 0.328,
    "model_score": 0.3423,
    "style_score": 0.3333,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I agree with this guy. Went to a career fair once and talked to a coup"
  },
  {
    "status": 200,
    "content_id": "aba867c7-a4cc-4073-b328-5ab310b1e9ac",
    "guess": "unsure",
    "combined_score": 0.3956,
    "confidence": 0.2088,
    "model_score": 0.3211,
    "style_score": 0.4276,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "While I generally agree with you, I'm calling cap on 240k\n There has t"
  },
  {
    "status": 200,
    "content_id": "e6653f3d-6c7b-417a-8656-b52e6f488924",
    "guess": "unsure",
    "combined_score": 0.4958,
    "confidence": 0.0084,
    "model_score": 0.0969,
    "style_score": 0.6667,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "You work for them \ud83d\ude22 . Trying to make it so commenter takes down post. "
  },
  {
    "status": 200,
    "content_id": "95fd1bc6-32f8-438a-9dc4-59eba85d79b8",
    "guess": "unsure",
    "combined_score": 0.4892,
    "confidence": 0.0216,
    "model_score": 0.4113,
    "style_score": 0.5226,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "can yall stop fantasizing about 10 years ago. if you joined the market"
  },
  {
    "status": 200,
    "content_id": "0666479e-860f-4e18-9e4b-4d32357d8d9c",
    "guess": "human",
    "combined_score": 0.1364,
    "confidence": 0.7272,
    "model_score": 0.316,
    "style_score": 0.0594,
    "label": "This looks like it was written by a person. If you think we got that wrong, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I\u2019m not OP but the way I did it was a bit different: I\u2019d apply to regu"
  },
  {
    "status": 200,
    "content_id": "62c106ad-df4e-4ae5-94bd-589cf7ebd081",
    "guess": "unsure",
    "combined_score": 0.3306,
    "confidence": 0.3388,
    "model_score": 0.3265,
    "style_score": 0.3324,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "stress isn\u2019t the only possibility for this to occur. There is a strong"
  },
  {
    "status": 200,
    "content_id": "84888014-4eb9-4751-9632-52cafb5f2c08",
    "guess": "unsure",
    "combined_score": 0.2766,
    "confidence": 0.4468,
    "model_score": 0.1443,
    "style_score": 0.3333,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "There will be ppl in their 20s who complain one day this time is easy "
  },
  {
    "status": 200,
    "content_id": "94a287b1-6602-4b26-9867-0b8313040c43",
    "guess": "unsure",
    "combined_score": 0.3296,
    "confidence": 0.3408,
    "model_score": 0.4078,
    "style_score": 0.2961,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I\u2019m sorry to hear that but it\u2019s like some people listen to their favor"
  },
  {
    "status": 200,
    "content_id": "9ac96286-7d5b-4d12-b2c5-c46bd6a9fd52",
    "guess": "unsure",
    "combined_score": 0.4337,
    "confidence": 0.1326,
    "model_score": 0.1423,
    "style_score": 0.5586,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I am also under review. According to sources online for JPMC, under re"
  },
  {
    "status": 200,
    "content_id": "6a09b6b9-03dd-49c1-87ca-81d60d8c5cae",
    "guess": "unsure",
    "combined_score": 0.4475,
    "confidence": 0.105,
    "model_score": 0.5415,
    "style_score": 0.4072,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Hey, I applied for a SWE role the questions for the virtual interview "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "content_id": "5a59301d-b60e-4e5d-83ed-fb58dd665637",
    "guess": "unsure",
    "combined_score": 0.336,
    "confidence": 0.328,
    "model_score": 0.3423,
    "style_score": 0.3333,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I agree with this guy. Went to a career fair once and talked to a coup"
  },
  {
    "status": 200,
    "content_id": "a70570c9-b7de-4f97-bbc9-fe28d60c4045",
    "guess": "unsure",
    "combined_score": 0.3956,
    "confidence": 0.2088,
    "model_score": 0.3211,
    "style_score": 0.4276,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "While I generally agree with you, I'm calling cap on 240k\n There has t"
  },
  {
    "status": 200,
    "content_id": "a8b87235-6cb9-44af-a6ac-f107a4a2f36a",
    "guess": "unsure",
    "combined_score": 0.4958,
    "confidence": 0.0084,
    "model_score": 0.0969,
    "style_score": 0.6667,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "You work for them \ud83d\ude22 . Trying to make it so commenter takes down post. "
  },
  {
    "status": 200,
    "content_id": "3b01167e-1510-4447-9e4d-7c3d53eed457",
    "guess": "unsure",
    "combined_score": 0.4892,
    "confidence": 0.0216,
    "model_score": 0.4113,
    "style_score": 0.5226,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "can yall stop fantasizing about 10 years ago. if you joined the market"
  },
  {
    "status": 200,
    "content_id": "848e3202-111a-4c7b-bd6b-e5aef6cf79ac",
    "guess": "human",
    "combined_score": 0.1364,
    "confidence": 0.7272,
    "model_score": 0.316,
    "style_score": 0.0594,
    "label": "This looks like it was written by a person. If you think we got that wrong, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I\u2019m not OP but the way I did it was a bit different: I\u2019d apply to regu"
  },
  {
    "status": 200,
    "content_id": "967e9ed1-3803-4ad9-85a1-513a2bce0099",
    "guess": "unsure",
    "combined_score": 0.3306,
    "confidence": 0.3388,
    "model_score": 0.3265,
    "style_score": 0.3324,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "stress isn\u2019t the only possibility for this to occur. There is a strong"
  },
  {
    "status": 200,
    "content_id": "4217da7d-2326-4aad-819e-08bac3bfb575",
    "guess": "unsure",
    "combined_score": 0.2766,
    "confidence": 0.4468,
    "model_score": 0.1443,
    "style_score": 0.3333,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "There will be ppl in their 20s who complain one day this time is easy "
  },
  {
    "status": 200,
    "content_id": "559c34dc-6b91-4d9c-8864-a7d221fabca1",
    "guess": "unsure",
    "combined_score": 0.3296,
    "confidence": 0.3408,
    "model_score": 0.4078,
    "style_score": 0.2961,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I\u2019m sorry to hear that but it\u2019s like some people listen to their favor"
  },
  {
    "status": 200,
    "content_id": "25425de4-cc2e-4afe-8926-b5453775f630",
    "guess": "unsure",
    "combined_score": 0.4337,
    "confidence": 0.1326,
    "model_score": 0.1423,
    "style_score": 0.5586,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "I am also under review. According to sources online for JPMC, under re"
  },
  {
    "status": 200,
    "content_id": "a0ccaa8c-e1a0-4457-826f-f0cf9fccdef6",
    "guess": "unsure",
    "combined_score": 0.4475,
    "confidence": 0.105,
    "model_score": 0.5415,
    "style_score": 0.4072,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Hey, I applied for a SWE role the questions for the virtual interview "
  }
]
```

### c2 AI half

**Trial 1**

```json
[
  {
    "status": 200,
    "content_id": "7fcf94d6-bad4-4b7f-9527-d5fe1c460248",
    "guess": "ai",
    "combined_score": 0.8442,
    "confidence": 0.6884,
    "model_score": 0.7825,
    "style_score": 0.8707,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Effective budgeting is a cornerstone of financial stability. By tracki"
  },
  {
    "status": 200,
    "content_id": "d29fc842-367b-4e37-92bb-2ee88d008a95",
    "guess": "ai",
    "combined_score": 0.8963,
    "confidence": 0.7926,
    "model_score": 0.9002,
    "style_score": 0.8946,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Regular physical activity offers a wide range of benefits for both the"
  },
  {
    "status": 200,
    "content_id": "197179d6-b389-430d-a3f8-f826e09e867b",
    "guess": "ai",
    "combined_score": 0.9333,
    "confidence": 0.8666,
    "model_score": 0.8505,
    "style_score": 0.9688,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Artificial intelligence is transforming industries across the globe. F"
  },
  {
    "status": 200,
    "content_id": "8511e590-2fb3-40c8-ac63-e806e840893e",
    "guess": "ai",
    "combined_score": 0.861,
    "confidence": 0.722,
    "model_score": 0.7911,
    "style_score": 0.891,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Sleep plays a vital role in maintaining good health. During sleep, the"
  },
  {
    "status": 200,
    "content_id": "0ddf33ed-a3a0-4eb1-810d-e8f67a9fc7fe",
    "guess": "ai",
    "combined_score": 0.8953,
    "confidence": 0.7906,
    "model_score": 0.8392,
    "style_score": 0.9194,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Volunteering is a meaningful way to give back to the community. It all"
  },
  {
    "status": 200,
    "content_id": "c452758d-d585-48bf-85cd-2cd0bf094ea4",
    "guess": "ai",
    "combined_score": 0.8202,
    "confidence": 0.6404,
    "model_score": 0.8156,
    "style_score": 0.8221,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Effective leadership is essential for the success of any organization."
  },
  {
    "status": 200,
    "content_id": "cabb0ce7-5fca-49f8-b8b0-f28f2f746726",
    "guess": "unsure",
    "combined_score": 0.6925,
    "confidence": 0.385,
    "model_score": 0.8123,
    "style_score": 0.6412,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Traveling to new places can be an enriching experience. It exposes peo"
  },
  {
    "status": 200,
    "content_id": "258354aa-c810-4963-aa0f-bae822fa2057",
    "guess": "ai",
    "combined_score": 0.8757,
    "confidence": 0.7514,
    "model_score": 0.8114,
    "style_score": 0.9033,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Cybersecurity has become a critical concern for individuals and busine"
  },
  {
    "status": 200,
    "content_id": "ae45b0ce-9293-4408-8a32-9f2aead51e94",
    "guess": "ai",
    "combined_score": 0.8131,
    "confidence": 0.6262,
    "model_score": 0.823,
    "style_score": 0.8089,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Gardening is a rewarding hobby that offers numerous benefits. It provi"
  },
  {
    "status": 200,
    "content_id": "67eeb6e1-1158-4a1d-a0f9-3330b4192432",
    "guess": "unsure",
    "combined_score": 0.6865,
    "confidence": 0.373,
    "model_score": 0.7529,
    "style_score": 0.6581,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Public libraries serve as valuable resources for communities. They off"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "content_id": "b050d374-2e4c-4b8f-94e4-8b6fdc0d1ac3",
    "guess": "ai",
    "combined_score": 0.8442,
    "confidence": 0.6884,
    "model_score": 0.7825,
    "style_score": 0.8707,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Effective budgeting is a cornerstone of financial stability. By tracki"
  },
  {
    "status": 200,
    "content_id": "dd87d3c2-fc2c-4003-bc09-b05462e8cd55",
    "guess": "ai",
    "combined_score": 0.8963,
    "confidence": 0.7926,
    "model_score": 0.9002,
    "style_score": 0.8946,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Regular physical activity offers a wide range of benefits for both the"
  },
  {
    "status": 200,
    "content_id": "3ff92d01-66d3-4c9a-ab1a-6ff94264dba4",
    "guess": "ai",
    "combined_score": 0.9333,
    "confidence": 0.8666,
    "model_score": 0.8505,
    "style_score": 0.9688,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Artificial intelligence is transforming industries across the globe. F"
  },
  {
    "status": 200,
    "content_id": "3a4ac467-d800-403a-bdcd-468164900fd4",
    "guess": "ai",
    "combined_score": 0.861,
    "confidence": 0.722,
    "model_score": 0.7911,
    "style_score": 0.891,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Sleep plays a vital role in maintaining good health. During sleep, the"
  },
  {
    "status": 200,
    "content_id": "4fd5d878-5764-4e69-a080-d49909caf676",
    "guess": "ai",
    "combined_score": 0.8953,
    "confidence": 0.7906,
    "model_score": 0.8392,
    "style_score": 0.9194,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Volunteering is a meaningful way to give back to the community. It all"
  },
  {
    "status": 200,
    "content_id": "3233cac2-1c24-40e5-91e7-7885ac427cef",
    "guess": "ai",
    "combined_score": 0.8202,
    "confidence": 0.6404,
    "model_score": 0.8156,
    "style_score": 0.8221,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Effective leadership is essential for the success of any organization."
  },
  {
    "status": 200,
    "content_id": "6ad11a0a-b34f-4ed2-bab3-b0dbcdfa188e",
    "guess": "unsure",
    "combined_score": 0.6925,
    "confidence": 0.385,
    "model_score": 0.8123,
    "style_score": 0.6412,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Traveling to new places can be an enriching experience. It exposes peo"
  },
  {
    "status": 200,
    "content_id": "d2c92536-888f-4cd9-8536-0c56341eb446",
    "guess": "ai",
    "combined_score": 0.8757,
    "confidence": 0.7514,
    "model_score": 0.8114,
    "style_score": 0.9033,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Cybersecurity has become a critical concern for individuals and busine"
  },
  {
    "status": 200,
    "content_id": "1d5c908b-f2c8-4e9f-9caa-88323c79329d",
    "guess": "ai",
    "combined_score": 0.8131,
    "confidence": 0.6262,
    "model_score": 0.823,
    "style_score": 0.8089,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Gardening is a rewarding hobby that offers numerous benefits. It provi"
  },
  {
    "status": 200,
    "content_id": "13b45855-1ce0-4afe-b96c-3069d0216550",
    "guess": "unsure",
    "combined_score": 0.6865,
    "confidence": 0.373,
    "model_score": 0.7529,
    "style_score": 0.6581,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Public libraries serve as valuable resources for communities. They off"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "content_id": "db872cd7-7b96-4994-8352-c6650b6b6b48",
    "guess": "ai",
    "combined_score": 0.8442,
    "confidence": 0.6884,
    "model_score": 0.7825,
    "style_score": 0.8707,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Effective budgeting is a cornerstone of financial stability. By tracki"
  },
  {
    "status": 200,
    "content_id": "4cd27388-da65-4031-9056-64733c560346",
    "guess": "ai",
    "combined_score": 0.8963,
    "confidence": 0.7926,
    "model_score": 0.9002,
    "style_score": 0.8946,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Regular physical activity offers a wide range of benefits for both the"
  },
  {
    "status": 200,
    "content_id": "1c64cc98-9736-49d2-96dc-585e8a4d0a96",
    "guess": "ai",
    "combined_score": 0.9333,
    "confidence": 0.8666,
    "model_score": 0.8505,
    "style_score": 0.9688,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Artificial intelligence is transforming industries across the globe. F"
  },
  {
    "status": 200,
    "content_id": "53acfc24-323f-4f48-963a-fae8792f8b4e",
    "guess": "ai",
    "combined_score": 0.861,
    "confidence": 0.722,
    "model_score": 0.7911,
    "style_score": 0.891,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Sleep plays a vital role in maintaining good health. During sleep, the"
  },
  {
    "status": 200,
    "content_id": "c0661ef3-28a5-4a10-bfa5-57f9180096f5",
    "guess": "ai",
    "combined_score": 0.8953,
    "confidence": 0.7906,
    "model_score": 0.8392,
    "style_score": 0.9194,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Volunteering is a meaningful way to give back to the community. It all"
  },
  {
    "status": 200,
    "content_id": "aa27b64d-a5f1-4ce9-8d3a-c1292833b692",
    "guess": "ai",
    "combined_score": 0.8202,
    "confidence": 0.6404,
    "model_score": 0.8156,
    "style_score": 0.8221,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Effective leadership is essential for the success of any organization."
  },
  {
    "status": 200,
    "content_id": "5c5473d1-0857-4d9f-947a-71b473c1a348",
    "guess": "unsure",
    "combined_score": 0.6925,
    "confidence": 0.385,
    "model_score": 0.8123,
    "style_score": 0.6412,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Traveling to new places can be an enriching experience. It exposes peo"
  },
  {
    "status": 200,
    "content_id": "0a63ca38-faec-4822-9a93-117e782b89a3",
    "guess": "ai",
    "combined_score": 0.8757,
    "confidence": 0.7514,
    "model_score": 0.8114,
    "style_score": 0.9033,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Cybersecurity has become a critical concern for individuals and busine"
  },
  {
    "status": 200,
    "content_id": "65eeec23-93ce-48f1-9833-dd4dce5b603f",
    "guess": "ai",
    "combined_score": 0.8131,
    "confidence": 0.6262,
    "model_score": 0.823,
    "style_score": 0.8089,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Gardening is a rewarding hobby that offers numerous benefits. It provi"
  },
  {
    "status": 200,
    "content_id": "828a4470-2630-4a96-9859-0901f28b6825",
    "guess": "unsure",
    "combined_score": 0.6865,
    "confidence": 0.373,
    "model_score": 0.7529,
    "style_score": 0.6581,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Public libraries serve as valuable resources for communities. They off"
  }
]
```

### c3 label coverage

**Trial 1**

```json
[
  {
    "status": 200,
    "content_id": "dc8cd627-2885-4212-a2cf-005b0dad9033",
    "guess": "human",
    "combined_score": 0.107,
    "confidence": 0.786,
    "model_score": 0.3192,
    "style_score": 0.0161,
    "label": "This looks like it was written by a person. If you think we got that wrong, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Totally agree. I don\u2019t go to a T20 School, I don\u2019t consider myself a \u2018"
  },
  {
    "status": 200,
    "content_id": "f77713f7-d508-4f11-8f30-0eb22fcbecfc",
    "guess": "unsure",
    "combined_score": 0.6348,
    "confidence": 0.2696,
    "model_score": 0.7901,
    "style_score": 0.5682,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "My grandmother had a garden behind her house. Every summer we picked t"
  },
  {
    "status": 200,
    "content_id": "4d451f2a-d433-4822-8194-29c9e8c52877",
    "guess": "ai",
    "combined_score": 0.8779,
    "confidence": 0.7558,
    "model_score": 0.941,
    "style_score": 0.8508,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Climate change is one of the most pressing issues facing our world tod"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "content_id": "8cb397d7-c3fa-49fe-adcd-9263521d9f4a",
    "guess": "human",
    "combined_score": 0.107,
    "confidence": 0.786,
    "model_score": 0.3192,
    "style_score": 0.0161,
    "label": "This looks like it was written by a person. If you think we got that wrong, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Totally agree. I don\u2019t go to a T20 School, I don\u2019t consider myself a \u2018"
  },
  {
    "status": 200,
    "content_id": "3af983ca-7d4b-43cf-a076-21810186b72d",
    "guess": "unsure",
    "combined_score": 0.6348,
    "confidence": 0.2696,
    "model_score": 0.7901,
    "style_score": 0.5682,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "My grandmother had a garden behind her house. Every summer we picked t"
  },
  {
    "status": 200,
    "content_id": "e25111c1-f423-4840-9138-dc35f81cea34",
    "guess": "ai",
    "combined_score": 0.8779,
    "confidence": 0.7558,
    "model_score": 0.941,
    "style_score": 0.8508,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Climate change is one of the most pressing issues facing our world tod"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "content_id": "ed699d7e-b41c-4dbf-9306-99af8de050a4",
    "guess": "human",
    "combined_score": 0.107,
    "confidence": 0.786,
    "model_score": 0.3192,
    "style_score": 0.0161,
    "label": "This looks like it was written by a person. If you think we got that wrong, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "Totally agree. I don\u2019t go to a T20 School, I don\u2019t consider myself a \u2018"
  },
  {
    "status": 200,
    "content_id": "e9b6f173-0eb5-4b68-8d2d-fd708a35d2f3",
    "guess": "unsure",
    "combined_score": 0.6348,
    "confidence": 0.2696,
    "model_score": 0.7901,
    "style_score": 0.5682,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens a lot, especially with short or plainly written pieces, and it isn't an accusation. If you'd like a person to take a look, you can ask for a review.",
    "error": null,
    "message": null,
    "sent": "My grandmother had a garden behind her house. Every summer we picked t"
  },
  {
    "status": 200,
    "content_id": "fb3b6bd8-f0d6-433c-be12-bf1aedf8b5c1",
    "guess": "ai",
    "combined_score": 0.8779,
    "confidence": 0.7558,
    "model_score": 0.941,
    "style_score": 0.8508,
    "label": "This shows strong signs of being written with AI. Our check can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.",
    "error": null,
    "message": null,
    "sent": "Climate change is one of the most pressing issues facing our world tod"
  }
]
```

### c5 invalid input

**Trial 1**

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

**Trial 2**

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

**Trial 3**

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
