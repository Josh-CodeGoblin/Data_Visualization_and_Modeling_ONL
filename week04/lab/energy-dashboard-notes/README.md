# Week 4: Building energy explorer

This package contains the executed assignment notebook, the unchanged UCI dataset, four static figures, and a working four-figure Plotly Dash app. The audience is architecture students comparing early building design options.

## Open the analysis

Open `Lab - Building an Interactive Dashboard.ipynb` in Jupyter from this folder. Keep `data/ENB2012_data.xlsx` beside it at the same relative path. The notebook includes saved outputs from a successful fresh-kernel execution of every code cell, including the supplied dashboard launch cell.

The source data, calculations, chart checks, conclusion, two limitations and AI-use reflection are included. Review the written answers and confirm dataset novelty against any submissions outside the available class repository before submitting.

To install notebook dependencies in your notebook environment, run:

```python
%pip install "dash>=2.11,<5" "plotly>=5,<7" "pandas>=2,<3" "numpy>=1.24,<3" "openpyxl>=3.1,<4" "matplotlib>=3.9,<4" "seaborn>=0.13,<1"
```

Restart the kernel after installing, then run the cells in order. A fresh application opens on port 8055. If the standalone preview is already running there, stop that preview first or use another available port in the notebook launch cell. Keep the notebook kernel running while interacting with its app.

## Run the standalone dashboard

From this folder, with the notebook environment active:

```text
python app.py
```

Open http://127.0.0.1:8055. The local address works only on this computer; it is not a public submission URL. The app does not require an AI account, API key or network connection to load its data or charts. The source link leads to UCI.

Use the two height checkboxes to select 3.5 m, 7 m, both, or neither. All four charts and the sample-size summary update. The bottom conclusion is explicitly based on all records.

## Hosting files

Copy these files into the class fork's `dashboards/personal/` folder, preserving paths:

```text
app.py
requirements.txt
data/ENB2012_data.xlsx
data/README.md
```

The app loads its data relative to `app.py`, exposes `server = app.server`, and uses a guarded local launch block. Gunicorn is for Linux hosting and does not need to run on Windows.

After reviewing the files, commit and push those four files to the branch you intend to deploy. Create a separate Render Web Service, keeping the class-demo service:

| Setting | Value |
| --- | --- |
| Root directory | `dashboards/personal` |
| Runtime | Python |
| Build | `pip install -r requirements.txt` |
| Start | `gunicorn app:server --bind 0.0.0.0:$PORT` |
| Instance | Free, if available in the account |

Open the public deployment and repeat the all-data, 3.5 m, 7 m, empty and reset checks listed in `VALIDATION.md`. A successful local check does not establish that the hosted version works.

## Before submission

- Confirm the dataset was not used in any earlier course work outside the checked repository.
- Review the code, explanations and AI-use reflection in your own words.
- Complete public deployment and add both the existing class-demo URL and the new personal-dashboard URL to the notebook.
- Submit the notebook, original dataset and runnable app code as required. Include supporting files and both public URLs.

The deadline shown in the assignment is October 25, 2026, 10:59 PM CDT.

## Course folder copy

A separate completed notebook named `Lab - Building an Interactive Dashboard - Energy.ipynb` was saved under the course repository's `week04/lab/`. The original open assignment notebook was preserved. The validated app and source data were also placed in `dashboards/personal/`; these changes have not been committed or pushed.

## Sources

Tsanas, A. & Xifara, A. (2012). [Energy Efficiency](https://archive.ics.uci.edu/dataset/242/energy+efficiency). UCI Machine Learning Repository. [Dataset DOI](https://doi.org/10.24432/C51307). CC BY 4.0.

[Original study](https://doi.org/10.1016/j.enbuild.2012.03.003), [Dash callbacks](https://dash.plotly.com/basic-callbacks), [Dash in Jupyter](https://dash.plotly.com/dash-in-jupyter).
