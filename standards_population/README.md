# Standards and Population Data

This project analyzes a JSON population dataset containing demographic fields and recent measurements for 152,361 individuals. The analysis examines age and weight distributions and investigates unusual observations.

## Contents

- `code.py` — descriptive statistics, histograms, a weight-versus-age scatter plot, and outlier lookup.
- `population.json` — source population records.

Run the code from this directory so the relative path to `population.json` resolves correctly. The current script displays figures interactively and does not write image files.

## Findings

Age histograms showed a sharp decrease around age 70; ten bins were selected for a readable view of that pattern. Weight showed a sharp peak near 68, and 22,613 records have a weight of exactly 68.0. The age-versus-weight analysis identified one unusual adult observation: Anthony Freeman (ID 1002902), age 41.3 and weight 21.7. The record merits validation, but the plot alone cannot establish whether it is erroneous.
