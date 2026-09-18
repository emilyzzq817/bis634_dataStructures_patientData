import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
# 1. Read XML
tree = ET.parse("patients.xml")
root = tree.getroot()

# 2. Find patients and extract ages
patients = root.find("patients")

ages = []
for patient in patients:
    age = patient.attrib["age"]
    ages.append(float(age))

# 3. Plot histogram
plt.hist(ages, bins=10)
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.title("Distribution of Patient Ages")
plt.savefig("age_histogram.png")
plt.show()