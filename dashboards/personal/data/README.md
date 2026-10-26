# Energy Efficiency source data

Tsanas, A. & Xifara, A. (2012). Energy Efficiency. UCI Machine Learning Repository.
https://doi.org/10.24432/C51307
https://archive.ics.uci.edu/dataset/242/energy+efficiency
Accessed October 25, 2026. License: CC BY 4.0.

Original file: ENB2012_data.xlsx, retained unchanged from the UCI download.
SHA-256: `0089fcffc1415e41e2ff63730cca5280efe54fc43d722dfde1b0aaa808e35dc4`
768 rows, 8 features, 2 outcomes. One row is an Ecotect-simulated building configuration.

X1 relative compactness (dimensionless); X2 surface area, X3 wall area and X4 roof area (m²); X5 overall height (m); X6 orientation code (2–5); X7 glazing/floor-area ratio; X8 glazing distribution (0 none, 1 uniform, 2 north, 3 east, 4 south, 5 west); Y1 heating load; Y2 cooling load. UCI does not specify physical load units, so the app uses source units.

No records are removed or imputed. The dashboard makes a copy, renames X5/X7/Y1/Y2, calculates X7 × 100 and adds original row IDs. All source columns are preserved. No sampling or joins.
