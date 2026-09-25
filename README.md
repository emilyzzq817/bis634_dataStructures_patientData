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
