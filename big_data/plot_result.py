import matplotlib.pyplot as plt

# 每一行：(filter size in bits, Misidentified %, Good Suggestion %)
results = {
    1: [
        (100_000, 98.91, 0.00),
        (1_000_000, 36.93, 0.00),
        (5_000_000, 8.65, 0.00),
        (10_000_000, 4.46, 0.33),
        (11_000_000, 4.18, 0.65),
        (20_000_000, 2.28, 7.91),
        (30_000_000, 1.53, 21.85),
        (100_000_000, 0.46, 73.41),
        (200_000_000, 0.20, 83.89),
        (250_000_000, 0.18, 85.46),
    ],
    2: [
        (100_000, 100.00, 0.00),
        (1_000_000, 36.87, 0.00),
        (5_000_000, 2.89, 3.42),
        (10_000_000, 0.78, 54.73),
        (11_000_000, 0.73, 62.16),
        (20_000_000, 0.20, 84.78),
        (30_000_000, 0.09, 87.72),
        (100_000_000, 0.00, 88.88),
        (200_000_000, 0.00, 88.95),
        (250_000_000, 0.00, 88.95),
    ],
    3: [
        (100_000, 100.00, 0.00),
        (1_000_000, 42.90, 0.00),
        (5_000_000, 1.39, 24.76),
        (10_000_000, 0.20, 84.54),
        (11_000_000, 0.17, 85.93),
        (20_000_000, 0.02, 88.66),
        (30_000_000, 0.00, 88.87),
        (100_000_000, 0.00, 88.97),
        (200_000_000, 0.00, 88.97),
        (250_000_000, 0.00, 88.97),
    ],
}

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

for k, rows in results.items():
    sizes = [row[0] for row in rows]
    misidentified = [row[1] for row in rows]
    good_suggestions = [row[2] for row in rows]

    axes[0].plot(sizes, misidentified, marker="o", label=f"k={k}")
    axes[1].plot(sizes, good_suggestions, marker="o", label=f"k={k}")

axes[0].set_title("Misidentified Percent")
axes[0].set_ylabel("Misidentified (%)")

axes[1].set_title("Good Suggestion Percent")
axes[1].set_ylabel("Good suggestions (%)")
axes[1].axhline(85, color="gray", linestyle="--", label="85% target")

for ax in axes:
    ax.set_xscale("log")
    ax.set_xlabel("Bloom filter size (bits)")
    ax.set_ylim(-2, 102)
    ax.grid(True, alpha=0.3)
    ax.legend()

plt.tight_layout()
plt.savefig("bloom_filter_results.png", dpi=200)
plt.show()