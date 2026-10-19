# Week 2 lab files

Both notebooks include saved outputs and completed code and written responses. Review the AI-assisted explanations before submission so you can explain the methods and results.

## Important assignment-version check

The local distributions notebook requires a new documented dataset and three investigations. It differs from the assignment screenshot, which describes NYC 311 requests. This completed version follows the local notebook and uses UCI Iris. Confirm that this is the instructor's intended version and that Iris was not used in class or in submissions outside the available repository. A search of 21 local notebook files found no Iris references in their code or Markdown.

## Files and verification

- `Lab - Relationships Between Categorical Features.ipynb`: 35 code cells executed in order without errors. Revised six-feature filters return one high-profile candidate and four low-profile candidates. The selected records are Helen Loraine Allison (298) and Daniel Coxon (95), both with `Survived = 0`. Includes completed evidence/profile tables, age boundaries, comparisons, biographies, conclusions, limitations, and AI disclosure. Existing working code and comments were retained where applicable; the age count chart was moved alongside the age percentage chart.
- `Lab - Comparing Distributions Across Groups.ipynb`: 27 code cells executed in order without errors. Three investigations compare sepal length, sepal width, and petal length across three iris species, with 50 plants per species. Includes six plots, grouped summaries/IQRs, original-record checks, all six workflow steps per question, citations, and AI disclosure.
- `data/titanic_passengers.csv`: copy of the supplied data.
- `data/iris.csv`: the original headerless comma-separated UCI file, preserved unchanged.
- `data/iris.names`: the original UCI dictionary, including documented discrepancies. The notebook corrects only three values in a separate analysis DataFrame and shows the before/after records.

All 13 plots were visually reviewed. Verification used Python 3.12, Pandas 3.0.6, Matplotlib 3.11.2, and Seaborn 0.13.2. Older Pandas versions may report text columns as `object` instead of `str`.

## Open and run

Keep the notebooks alongside the `data` folder. Extract the ZIP before opening either notebook. In Jupyter, restart the kernel and run all cells from top to bottom. The distributions notebook needs Pandas, Matplotlib, and Seaborn.

To switch to the original repository folder in Anaconda Prompt:

```bat
cd /d D:\GitHubBase\Data_Visualization_and_Modeling_ONL\week02\lab
jupyter notebook
```

The completed files were saved separately; the original D-drive notebooks were not overwritten. To use the completed copies in your repository, back up the originals, then copy these two notebooks and the new Iris data/dictionary into `week02/lab`, preserving the `data` subfolder.

The assignment screenshot requests a GitHub link and shows late submissions closed. These files have not been pushed to GitHub or submitted. Confirm submission arrangements with the instructor.

## Sources

- UCI Iris dataset: https://archive.ics.uci.edu/dataset/53/iris
- UCI raw data: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
- UCI dictionary: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names
- Helen Loraine Allison: https://www.encyclopedia-titanica.org/titanic-victim/loraine-allison.html
- Daniel Coxon: https://www.encyclopedia-titanica.org/titanic-victim/daniel-coxon.html

Sources accessed October 13, 2026. UCI credits R. A. Fisher (1936); Iris is licensed CC BY 4.0.
