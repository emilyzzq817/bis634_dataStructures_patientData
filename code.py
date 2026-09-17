import xml.etree.ElementTree as ET
tree = ET.parse("patients.xml")
root = tree.getroot()

print(root.tag)

for child in root:
    print(child.tag, child.attrib)

patients = root.find("patients")

print(patients.tag)

for patient in patients:
    print(patient.tag, patient.attrib)

first_patient = patients[0]

for child in first_patient:
    print(child.tag, child.attrib, child.text)

ages = []

for patient in patients:
    age = patient.attrib["age"]
    ages.append(float(age))

print(ages[:5])

import matplotlib.pyplot as plt

plt.hist(ages, bins=10)
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.title("Distribution of Patient Ages")
plt.show()
