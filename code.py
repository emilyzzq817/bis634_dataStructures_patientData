import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from collections import Counter

# 1a. 
# eead XML
tree = ET.parse("patients.xml")
root = tree.getroot()

# find patients and extract ages
patients = root.find("patients")

ages = []
for patient in patients:
    age = patient.attrib["age"]
    ages.append(float(age))

# 3. plot histogram
plt.hist(ages, bins=10)
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.title("Distribution of Patient Ages")
plt.savefig("age_histogram.png")
plt.show()


# 1b. 
genders = []

for patient in patients:
    gender = patient.findtext("gender")
    genders.append(gender)

gender_counts = Counter(genders)

print("Distinct gender categories:", list(gender_counts.keys()))
print("Gender counts:", gender_counts)

plt.bar(gender_counts.keys(), gender_counts.values())
plt.title("Distribution of Patient Genders")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.show()