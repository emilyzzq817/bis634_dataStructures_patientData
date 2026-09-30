import json
import statistics
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent

# 2b.
with open(PROJECT_DIR / "population.json") as f:
    population = json.load(f)

ages = [person["demographics"]["age"] for person in population]

print("Mean:", statistics.mean(ages))
print("Standard deviation:", statistics.stdev(ages))
print("Minimum:", min(ages))
print("Maximum:", max(ages))

# for bins in [5, 10, 15, 20]:
#     plt.hist(ages, bins=bins)
#     plt.title(f"Age distribution ({bins} bins)")
#     plt.xlabel("Age")
#     plt.ylabel("Number of people")
#     plt.show()

# Final histogram: 10 bins
plt.figure(figsize=(8, 5))
plt.hist(ages, bins=10)
plt.title("Age distribution (10 bins)")
plt.xlabel("Age")
plt.ylabel("Number of people")
plt.tight_layout()
plt.savefig(PROJECT_DIR / "age_distribution.png", dpi=200)
plt.close()


# 2c. 
weights = [person["last_measurements"]["weight"] for person in population]

print("Mean:", statistics.mean(weights))
print("Standard deviation:", statistics.stdev(weights))
print("Minimum:", min(weights))
print("Maximum:", max(weights))

# for bins in [10,20,30,40]:
#     plt.hist(weights, bins=bins)
#     plt.title(f"Weight distribution ({bins} bins)")
#     plt.xlabel("Weight")
#     plt.ylabel("Number of people")
#     plt.show()

# Final histogram: 30 bins
plt.figure(figsize=(8, 5))
plt.hist(weights, bins=30)
plt.title(f"Weight distribution (30 bins)")
plt.xlabel("Weight")
plt.ylabel("Number of people")
plt.tight_layout()
plt.savefig(PROJECT_DIR / "weight_distribution.png", dpi=200)
plt.close()

#2d.
plt.figure(figsize=(8, 5))
plt.scatter(ages, weights, s=1)
plt.title("Weight versus age")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.tight_layout()
plt.savefig(PROJECT_DIR / "weight_vs_age.png", dpi=200)
plt.close()

for person in population:
    age = person["demographics"]["age"]
    weight = person["last_measurements"]["weight"]

    if age > 30 and weight < 30:
        print(person["name"], person["id"], age, weight)
