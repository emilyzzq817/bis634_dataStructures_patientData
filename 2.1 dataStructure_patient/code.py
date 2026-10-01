import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent

# 1a. Parse XML & Analyze Age Distribution
tree = ET.parse(PROJECT_DIR / "patients.xml")
root = tree.getroot()

patients = root.find("patients")

ages = []
for patient in patients:
    age = patient.attrib["age"]
    ages.append(float(age))

age_counts = Counter(ages)
duplicate_age_values = sum(count > 1 for count in age_counts.values())
print("Exact duplicate age values:", duplicate_age_values)

plt.hist(ages, bins=10)
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.title("Distribution of Patient Ages")
plt.savefig(PROJECT_DIR / "age_histogram.png")
plt.show()


# 1b. Analyze Gender Distribution
genders = []

for patient in patients:
    gender = patient.attrib["gender"]
    genders.append(gender)

gender_counts = Counter(genders)

categories = list(gender_counts.keys())
counts = list(gender_counts.values())

print("Distinct gender categories:", categories)
print("Gender counts:", gender_counts)

plt.figure(figsize=(8, 5))
plt.bar(
    categories,
    counts,
    color=["mediumpurple", "coral", "lightgray"],
    edgecolor="white"
)
plt.title("Distribution of Patient Genders")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.savefig(PROJECT_DIR / "gender_bar.png")
plt.show()


# 1c. Age Sorting & Top-K Retrieval
def get_age(patient):
    return float(patient.attrib["age"])
patients_sorted_by_age = sorted(patients, key=get_age)

oldest_patient = patients_sorted_by_age[-1]

print("Oldest patient:", oldest_patient.attrib)
print("Name:", oldest_patient.attrib["name"])
print("Age:", oldest_patient.attrib["age"])
print("Gender:", oldest_patient.attrib["gender"])


# 1d. Algorithmic Trade-offs: Finding the Second-Oldest Patient
oldest_patient_linear = None
second_oldest_patient = None

oldest_age = 0
second_oldest_age = 0

for patient in patients:
    age = get_age(patient)

    if age > oldest_age:
        second_oldest_patient = oldest_patient_linear
        second_oldest_age = oldest_age

        oldest_patient_linear = patient
        oldest_age = age

    elif oldest_age > age > second_oldest_age:
        second_oldest_patient = patient
        second_oldest_age = age

print("Second-oldest patient:", second_oldest_patient.attrib)
print("Name:", second_oldest_patient.attrib["name"])
print("Age:", second_oldest_patient.attrib["age"])
print("Gender:", second_oldest_patient.attrib["gender"])

# 1e. Binary search for age 41.5
age_index = [get_age(patient) for patient in patients_sorted_by_age]

def binary_search_left(age_index, target_age):
    left = 0
    right = len(age_index)

    while left < right:
        middle = (left + right) // 2

        if age_index[middle] < target_age:
            left = middle + 1
        else:
            right = middle

    return left

target_age = 41.5
target_index = binary_search_left(age_index, target_age)

if target_index < len(age_index) and age_index[target_index] == target_age:
    patient_41_5 = patients_sorted_by_age[target_index]
    print("Patient aged 41.5:", patient_41_5.attrib)
else:
    print("No patient is exactly 41.5 years old.")

# 1f. Count patients age 41.5 or older
patients_at_least_41_5 = len(age_index) - target_index

print("Patients aged 41.5 or older:", patients_at_least_41_5)

# 1g. Count patients in an age range [low_age, high_age)
def count_age_range(low_age, high_age):
    if low_age >= high_age:
        return 0

    low_index = binary_search_left(age_index, low_age)
    high_index = binary_search_left(age_index, high_age)

    return high_index - low_index

# Test cases
print("Patients aged 41.5 to under 50:", count_age_range(41.5, 50))
print("Patients aged 0 to under 100:", count_age_range(0, 100))
print("Patients aged 90 to under 100:", count_age_range(90, 100))
print ("Empty range [41.5, 41.5):",count_age_range(41.5, 41.5))


# 1h. Build a prefix sum for male patients
male_prefix = [0]

for patient in patients_sorted_by_age:
    is_male = patient.attrib["gender"] == "male"
    male_prefix.append(male_prefix[-1] + is_male)

def count_age_and_male_range(low_age, high_age):
    if low_age >= high_age:
        return 0, 0

    low_index = binary_search_left(age_index, low_age)
    high_index = binary_search_left(age_index, high_age)

    total_count = high_index - low_index
    male_count = male_prefix[high_index] - male_prefix[low_index]

    return total_count, male_count

# Example test
total, male = count_age_and_male_range(41.5, 50)
print("Total patients aged 41.5 to under 50:", total)
print("Male patients aged 41.5 to under 50:", male)
