# BIS 634 Portfolio: Data Structures Patient Data

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

## Data Structures Exercise Notes

### Histogram of patient ages

![Histogram of Patient Ages](age_histogram.png)

I explored histograms with 5, 10, and 20 bins. I selected 10 bins because it provided enough detail to show the age distribution without making the histogram overly fragmented.

### Gender distribution

Gender is encoded as a `gender` attribute within each `<patient>` record, rather than as a patient element. The distinct categories in the XML dataset were printed by the analysis code. A bar chart was used because gender is categorical data.

![Bar of Gender distribution](gender_bar.png)

### Sorting and top-k retrieval

The `get_age()` function extracts each patient's `age` attribute and converts it to a float. Sorting with this function as the key orders patients from youngest to oldest; numeric conversion is necessary because XML attributes are strings. The final record in the sorted list is the oldest patient.

For a single request to find the second-oldest patient, an O(n) single-pass approach is more efficient because it examines each record once without sorting the complete dataset. If many later queries require age order, sorting once in O(n log n) time enables O(1) position lookups.

### Binary search and range queries

The left-bound binary search returns the first position where 41.5 can be inserted while preserving age order. If an exact match exists, this is the first matching patient; otherwise it is the insertion point. The number of patients aged 41.5 or older is `len(age_index) - target_index`, calculated in O(1) after the O(log n) search.

For a range `[low_age, high_age)`, two binary searches locate the bounds and their index difference gives the count. The code tests normal, full-dataset, out-of-bounds, and empty ranges. A prefix sum for male patients supports age-and-gender range queries: its O(n) construction is performed once, then each query uses two binary searches and O(1) prefix-sum subtraction.
