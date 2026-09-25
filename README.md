# bis634_dataStructures

## 1a. Histogram of Patient Ages

![Histogram of Patient Ages](age_histogram.png)
I explored histograms with 5, 10, and 20 bins. I selected 10 bins because it provided enough detail to show the age distribution without making the histogram overly fragmented.

### 1b. Gender distribution

Gender is encoded as a `gender` attribute within each `<patient>` record, rather than as a patient element. The distinct categories in the XML dataset were `[... ]`. I used a bar chart because gender is categorical data.

### 1c. 
I used `get_age()` function to extract the `age` attribute from each patient record and converts it to a float. I then used `sorted()` with this function as its sorting key to create an ordered list `patients_sorted_by_age`from youngest to oldest. Converting age to a float was needed because XML attributes are read as strings; string sorting would not preserve numeric age order. The final record in the sorted list was the oldest patient. The output identified this patient as **[name]**, age **[age]**, gender **[gender]**.
![Bar of Gender distribution](gender_bar.png)


### 1d. 
For a single request to find the second-oldest patient, the O(n) single-pass approach is more efficient because it examines each record once without sorting the full dataset. However, if many later queries require patients to be ordered by age, it is more useful to sort once in O(n log n) time. After sorting, retrieving a patient at a known position, such as the oldest or second-oldest patient, using O(1) lookups.
