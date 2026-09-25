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


### 1e. 

I first used the patient list sorted in 1c. to create `age_index`, which contains the ages in ascending order. During the search, I compared 41.5 with the middle value of the remaining section of the index. Each comparison removed half of the possible locations, so the search itself takes O(log n) time.

My function returns the first position where 41.5 could be placed while preserving the age order. If an exact 41.5 value is present, that position
corresponds to the first matching patient. If several patients have the same age, starting at the first match makes the result consistent. If 41.5 is not present, the returned position is where it would be inserted, and the equality check reports that there is no exact match.


### 1f.
The left-bound binary search returns the index of the first age that is greater than or equal to 41.5. Because `age_index` is sorted in ascending order, every record from that index through the end of the list is at least 41.5 years old. Therefore, I calculated the count as `len(age_index) - target_index`. This calculation takes O(1) time after the O(log n) binary search. The dataset contained **150,471** patients aged 41.5 or older.


### 1g. 
I wrote `count_age_range(low_age, high_age)` to count patients with `low_age ≤ age < high_age`. I used binary search to find where the lower and upper age bounds would be in the sorted age list. The number of patients in the range is the difference between these two positions.

I tested a normal range, `[41.5, 50)`, a range covering the full dataset, `[0, 100)`, an out-of-bounds range, `[90, 100)`, and an empty range, `[41.5, 41.5)`. The empty range returns zero. Each query remains O(log n) because it performs two O(log n) binary searches and then one O(1) subtraction.

### 1h. Age and gender range queries
I wanted to count male patients in an age range without checking every patient in that range one by one. After sorting the patients by age, I made a list called `male_prefix`. As I move through the sorted list, this list keeps track of how many male patients have appeared so far.

For each age query, I use binary search to find the beginning and end of the requested range. The total number of patients is the difference between those two indices. To get the male count, I subtract the number of males before the start of the range from the number of males before the end of the range.

Creating `male_prefix` takes O(n) time once. After that, each query uses two binary searches, so it takes O(log n) time.
