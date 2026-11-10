## Milestone 3: Evaluation and Results

Milestone 3 is complete and has been pushed to GitHub (commit `e19f631`).

I ran the evaluation suite three times, and all five acceptance criteria were met consistently across all three runs.

### Evaluation Results

| Criterion | Target | Result | Status |
|---|---|---|---|
| Human writing incorrectly labeled AI | ≤ 1/20 | 0/20 | Passed |
| AI–human mean score separation | ≥ 0.25 | 0.479 | Passed |
| All three classification labels reached | 3/3 | 3/3 | Passed |
| Appeals recorded and marked under review | 10/10 | 10/10 | Passed |
| Invalid inputs rejected without a decision | 5/5 | 5/5 | Passed |

The mean AI score was 0.828, compared with 0.349 for human writing. All three evaluation runs produced identical results.

### Worst-Failure Analysis: FP03

One particularly interesting case was FP03, a genuine human-written account of someone's first month in a new country.

The detector returned:
- **Model signal:** 0.805
- **Stylometric signal:** 0.614
- **Combined score:** 0.709
- **Final classification:** Unsure

Although the system avoided incorrectly labeling the writing as AI-generated, the combined score was relatively close to the AI classification threshold of 0.80.

This raises an important concern about whether careful, straightforward writing, particularly from non-native English speakers, might be disproportionately flagged by the detector.

My next step is to investigate which component of the pipeline contributes most to this behavior. I'll compare the individual signals, examine the stylometric features, and test alternative weighting schemes to determine whether the issue is isolated or systematic.

### Next Steps

For Milestone 4, I'll focus on identifying recurring patterns across the highest-scoring human samples, understanding the causes of false-positive risk, and evaluating possible improvements without sacrificing the system's ability to distinguish AI-generated writing from human writing.
