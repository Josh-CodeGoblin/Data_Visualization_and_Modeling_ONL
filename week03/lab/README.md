# Week 3: Relationships Between Quantitative Features

This lab uses 62 historical mammal species records to investigate sleep phases, danger and predation categories, and gestation time. Each row represents a species rather than an individual animal.

## Open the lab

Open [the completed notebook](Lab%20-%20Relationships%20Between%20Quantitative%20Features.ipynb). Saved tables and all nine plots are included for viewing on GitHub.

To run it locally:

1. Install the packages in `requirements.txt` in a Python environment.
2. Start Jupyter from this `week03/lab` directory and open the notebook.
3. Restart the kernel and run all cells in order.

The notebook loads `data/mammal_sleep.csv` using a relative path. Keep the notebook and its `data` folder together. The requirements file covers this quantitative-features lab only.

## Investigations and results

| Investigation | Observations | Main result |
| --- | ---: | --- |
| Dreaming, non-dreaming, and total sleep | 48 | Non-dreaming versus total sleep: r = 0.963, R² = 0.927 |
| Danger and predation beyond non-dreaming sleep | 48 | R² = 0.927 baseline, 0.943 with danger, 0.937 with predation, 0.951 with both |
| Gestation and total sleep | 54 | R² = 0.399 for original gestation, 0.440 for log10 gestation, 0.694 for log10 gestation plus both categories |

The additive models treat the ratings as categories and share a quantitative-predictor slope. The plotted group regressions can have separate slopes. All model comparisons within an investigation use identical observations. These are in-sample fits, not evidence of causation or validated predictions. Total sleep includes non-dreaming sleep, which contributes to their strong relationship.

## Data and attribution

The CSV is the existing course-supplied dataset, retained unchanged in this course fork. The [course repository](https://github.com/Chelsea-Myers/Data_Visualization_and_Modeling_ONL) directs students to fork it and save their notebook changes. Its public data and notebook instructions were checked during this review. No separate dataset redistribution license was found; no new license or broader reuse permission is asserted here.

The course dataset preserves the historical records with descriptive column names and blank fields in place of the source's `-999` missing codes. See the [original data](https://www.stat.berkeley.edu/~spector/s100/data/sleep.dat), [measurement dictionary](https://www.stat.berkeley.edu/~spector/s100/data/sleep.html), and [Allison and Cicchetti (1976)](https://pubmed.ncbi.nlm.nih.gov/982039/).

## Review and AI assistance

On October 18, 2026 (America/Chicago), the reviewed notebook ran in a fresh kernel with all 31 code cells completing successfully and nine plots produced. The review checked missing values, subsets, correlations, R², additive models, category counts and ranges, sleep-phase sums, and reverse-log calculations. The plots were visually inspected.

AI assisted with review and corrections, as disclosed in the notebook. The original Investigation 2 prediction was not recorded or remembered, so the answer explicitly says so. This remains a limitation relative to the assignment's request for a before-analysis prediction.

Validated with Python 3.13.9 and the package versions in `requirements.txt`.
