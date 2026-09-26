import json
import statistics
import matplotlib.pyplot as plt

# 2b.
with open("population.json") as f:
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

# Final histogram: 15 bins
plt.hist(ages, bins=15)
plt.title("Age distribution (15 bins)")
plt.xlabel("Age")
plt.ylabel("Number of people")
plt.show()


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
plt.hist(weights, bins=30)
plt.title(f"Weight distribution (30 bins)")
plt.xlabel("Weight")
plt.ylabel("Number of people")
plt.show()

#2d.
plt.scatter(ages, weights, s=1)
plt.title("Weight versus age")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.show()

for person in population:
    age = person["demographics"]["age"]
    weight = person["last_measurements"]["weight"]

    if age > 30 and weight < 30:
        print(person["name"], person["id"], age, weight)