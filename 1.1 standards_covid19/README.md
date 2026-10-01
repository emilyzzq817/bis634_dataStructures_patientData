# COVID-19 State-Level Data

This project analyzes reported daily COVID-19 cases in California, Florida, and New York from a state-level cumulative case and death time series.

Data source: The New York Times COVID-19 data repository, `us-states.csv`. The dataset reports cumulative cases and deaths by state; the analysis derives daily new cases by differencing consecutive cumulative case totals.

Data source: The New York Times COVID-19 data repository, `us-states.csv`. The dataset reports cumulative cases and deaths by state; the analysis derives daily new cases by differencing consecutive cumulative case totals.

## Contents

- `covid_analysis.py` — calculates daily cases from cumulative totals, identifies peak dates, compares peak timing, checks Florida for negative daily counts, and saves the figure.
- `us-states.csv` — daily cumulative cases and deaths by U.S. state, with date, state, FIPS, cases, and deaths columns.
- `daily_cases_comparison.png` — daily-case comparison for the three coastal states.

Run `python3 covid_analysis.py` from this directory with `pandas` and `matplotlib` installed. The script resolves its data file relative to the script location and writes `daily_cases_comparison.png`.

## Development from studio work

The initial analysis loaded cumulative state totals and calculated daily differences. The final version organizes the work into reusable plotting and peak-date functions, compares California and New York peaks, checks Florida for negative daily values, formats the multi-year date axis, and saves the completed figure for the portfolio.

## Development from studio work

The initial analysis loaded cumulative state totals and calculated daily differences. The final version organizes the work into reusable plotting and peak-date functions, compares California and New York peaks, checks Florida for negative daily values, formats the multi-year date axis, and saves the completed figure for the portfolio.

## Findings

California's highest reported daily case count occurred on January 10, 2022. New York reached its daily-case peak before California. Florida includes a negative daily difference of -40,527 cases on June 4, 2021, which is best interpreted as a retrospective revision to a cumulative total rather than a real negative number of new cases.

Reported daily counts can be affected by reporting delays and backlogs. The dataset does not provide contextual factors such as testing availability, exposure risk, or public-health policies, so the visualization cannot by itself explain why trends changed.

The x-axis uses quarterly `YYYY-MM` labels so the multi-year time series remains readable.

The x-axis uses quarterly `YYYY-MM` labels so the multi-year time series remains readable.

![Daily new COVID-19 cases in coastal states](daily_cases_comparison.png)
