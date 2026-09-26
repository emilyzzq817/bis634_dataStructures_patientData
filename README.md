# BIS 634 Portfolio

Emily Zhang
NetID: zz598

This repository collects coursework for BIS 634: Computational Methods for Informatics. Each project keeps its code, data, figures, and project-specific documentation together.

## Projects

### [Patient Data and Data Structures](dataStructure_patient/)

Patient-record analysis using XML, sorting, binary search, and prefix sums.

- [Code](dataStructure_patient/code.py)
- [Patient data](dataStructure_patient/patients.xml)
- [Age histogram](dataStructure_patient/age_histogram.png)
- [Gender bar chart](dataStructure_patient/gender_bar.png)
- [Detailed analysis](dataStructure_patient/README.md)

### [Big Data and Bloom Filters](bigData/)

A Bloom-filter spelling-correction experiment that compares one, two, and three hash functions, evaluates false positives, and discusses privacy and performance trade-offs.

- [Code](bigData/code.py)
- [Evaluation/plot script](bigData/plot_result.py)
- [Word list](bigData/words.txt)
- [Typo-pair data](bigData/typos.json)
- [Evaluation figure](bigData/bloom_filter_results.png)
- [Detailed analysis](bigData/README.md)

### [Standards and Population Data](standards_population/)

Descriptive analysis of a population JSON dataset, including age and weight distributions and an outlier investigation.

- [Code](standards_population/code.py)
- [Population data](standards_population/population.json)
- [Detailed analysis](standards_population/README.md)

### [COVID-19 State-Level Data](standards_covid19/)

Analysis of reported daily COVID-19 cases in California, Florida, and New York, including peak-date comparison and a reporting-anomaly check.

- [Analysis code](standards_covid19/covid_analysis.py)
- [Dataset](standards_covid19/data/us-states.csv)
- [Daily-case comparison figure](standards_covid19/figures/daily_cases_comparison.png)
- [Project notes](standards_covid19/README.md)
