# Validation record

## Completed locally

- Read all 55 original assignment cells and both rubric screenshots. The notebook requires four static and four interactive figures, which is stricter than the brief LMS summary.
- Inspected available lecture and earlier lab notebooks in week01–week04. No prior use of UCI Energy Efficiency was found. Separate submissions not in that repository remain for the student to confirm.
- Confirmed 768 records, 10 columns, no missing values, and no exact duplicate rows. Preserved the original workbook and recorded its SHA-256 in the data README and notebook output.
- Executed all 13 code cells in a fresh Python kernel, in order, without errors. This included the actual Dash Jupyter launch cell.
- Rendered and visually inspected all four Matplotlib/Seaborn figures. Labels, counts, group colors, glazing order and source-unit labels were checked.
- Independently checked one plotted value from each static figure using original records and Python arithmetic.
- Checked every histogram bin, every box-plot input value, every scatter point, and every heatmap mean/count for both individual heights and all data. Confirmed the original DataFrame was unchanged.
- Exercised Dash's HTTP callback route for 3.5 m, 7 m, empty and reset. Each returned HTTP 200 and all five outputs.
- Tested the color revision by rebuilding fresh app instances: the 7 m series changed from gray to orange in the box/scatter views, with identical data and one registered callback.
- Opened the final standalone app in the browser. Clicked 3.5 m, 7 m, neither and both. Confirmed updated summaries and chart text; empty selection displayed four explanatory messages. Reset restored 768 records. No browser console errors were reported.
- Inspected the narrow single-column layout and the 1280-pixel two-column layout. Saved `dashboard-preview.png` from the all-data browser view.

## Numerical evidence

| Selection | n | Heating [10,15) count | Median heating for selected height | Cooling mean at 40% glazing |
| --- | ---: | ---: | ---: | ---: |
| 3.5 m only | 384 | 265 | 12.985 | 17.780083 |
| 7 m only | 384 | 0 | 31.675 | 36.042750 |
| Both heights | 768 | 265 | Separate medians above | Separate means above |
| Neither | 0 | No chart | No summary | No summary |

Loads are in source units. Each height's 40% glazing cell contains 120 designs. Original record 1 has height 7 m, 0% glazing and heating 15.55.

Browser summaries: all records, heating 22.31 and cooling 24.59; 3.5 m, 13.34 and 16.07; 7 m, 31.28 and 33.10. These are arithmetic means over the selected records.

## Still outstanding

- Public GitHub push and Render deployment have not been performed.
- The class-demo public URL was not found in the checked course files.
- Both hosted URLs must be added, and controls must be rechecked on the public personal service.
- The student must review the analysis, verify dataset novelty outside the available repository and personalize the AI-use reflection.

These local checks do not constitute a completed submission or proof of a public deployment.
