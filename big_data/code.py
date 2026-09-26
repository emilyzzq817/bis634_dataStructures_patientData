with open('words.txt') as f:
  words = [line.strip().lower() for line in f if line.strip()]

import string
from hashlib import blake2b, sha256, sha3_256
from bitarray import bitarray


class BloomFilter:
    def __init__(self, size: int, hash_count: int = 3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _get_hashes(self, item: str):
        s = item.lower().encode()
        hashes = [
            int(sha256(s).hexdigest(), 16) % self.size,
            int(blake2b(s).hexdigest(), 16) % self.size,
            int(sha3_256(s).hexdigest(), 16) % self.size,
        ]
        return hashes[: self.hash_count]

    def add(self, item: str):
        for h in self._get_hashes(item):
            self.bit_array[h] = True

    def __contains__(self, item: str) -> bool:
        return all(self.bit_array[h] for h in self._get_hashes(item))

def suggest_corrections(
    typed_word: str,
    bloom_filter: BloomFilter
) -> list[str]:
    matches = []
    word = typed_word.lower()

    for i in range(len(word)):
        for letter in string.ascii_lowercase:
            if letter == word[i]:
                continue

            candidate = word[:i] + letter + word[i + 1:]

            if candidate in bloom_filter:
                matches.append(candidate)

    return matches

# Part A
for k in (1, 2, 3):
    bloom_filter = BloomFilter(size=10**7, hash_count=k)

    for word in words:
        bloom_filter.add(word)

    print(f"{k} hash function(s):",
          suggest_corrections("floeer", bloom_filter))


# Part B
import json
import matplotlib.pyplot as plt

with open("typos.json", encoding="utf-8") as f:
    typo_pairs = json.load(f)



filter_sizes = [
    100_000, 1_000_000, 5_000_000,
    10_000_000, 11_000_000, 20_000_000, 30_000_000,
    100_000_000, 200_000_000, 250_000_000]
results = {1: [], 2: [], 3: []}

for k in (1,2,3): 
    for size in filter_sizes:
        bloom_filter = BloomFilter(size=size, hash_count=k)

        for word in words:
            bloom_filter.add(word)

        typo_count = 0
        misidentified_count = 0
        good_suggestion_count = 0

        for typed_word, correct_word in typo_pairs:
            if typed_word != correct_word:
                typo_count += 1
                if typed_word in bloom_filter:
                    misidentified_count += 1

            candidates = suggest_corrections(typed_word, bloom_filter)
            if typed_word in bloom_filter:
                candidates.append(typed_word)

            if len(candidates) <= 3 and correct_word in candidates:
                good_suggestion_count += 1

        misidentified_percent = 100 * misidentified_count / typo_count
        good_suggestion_percent = (
            100 * good_suggestion_count / len(typo_pairs)
        )

        results[k].append(
            (size, misidentified_percent, good_suggestion_percent)
        )

        print(
            f"k={k}, size={size:,}: "
            f"misidentified={misidentified_percent:.2f}%, "
            f"good suggestions={good_suggestion_percent:.2f}%"
        )