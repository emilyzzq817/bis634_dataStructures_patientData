# BIS 634 Portfolio

Emily Zhang
NetID: zz598

This repository collects coursework for BIS 634: Computational Methods for Informatics. Each project keeps its code, data, figures, and project-specific documentation together.

## Projects

### [Data Structures](.)

Patient-record analysis using XML, sorting, binary search, and prefix sums. The program parses the patient data, produces age and gender visualizations, and supports efficient age-range queries.

- [Code](code.py)
- [Patient data](patients.xml)
- [Age histogram](age_histogram.png)
- [Gender bar chart](gender_bar.png)

### [Big Data and Bloom Filters](big_data/)

A Bloom-filter spelling-correction experiment that compares one, two, and three hash functions, evaluates false positives, and discusses privacy and performance trade-offs.

- [Code](big_data/code.py)
- [Evaluation/plot script](big_data/plot_result.py)
- [Word list](big_data/words.txt)
- [Typo-pair data](big_data/typos.json)
- [Evaluation figure](big_data/bloom_filter_results.png)
- [Detailed analysis](big_data/README.md)

### [Standards and Population Data](standards_population/)

Descriptive analysis of a population JSON dataset, including age and weight distributions and an outlier investigation.

- [Code](standards_population/code.py)
- [Population data](standards_population/population.json)
- [Detailed analysis](standards_population/README.md)

### [COVID-19 State-Level Data](covid/)

Analysis of reported daily COVID-19 cases in California, Florida, and New York, including peak-date comparison and a reporting-anomaly check.

- [Analysis code](covid/covid_analysis.py)
- [Dataset](covid/data/us-states.csv)
- [Daily-case comparison figure](covid/figures/daily_cases_comparison.png)
- [Project notes](covid/README.md)
