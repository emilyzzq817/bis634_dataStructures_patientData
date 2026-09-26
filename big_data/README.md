# Big Data and Bloom Filters

This project builds a Bloom filter from a word list and uses it to generate one-character substitution suggestions for misspelled words. It compares filters using one, two, and three hash functions, evaluates false-positive behavior with the supplied typo pairs, and visualizes the experiment results.

## Contents

- `code.py` — Bloom filter implementation and evaluation workflow.
- `plot_result.py` — plotting helper for the evaluation results.
- `words.txt` — source vocabulary.
- `typos.json` — typo/correct-word pairs used for evaluation.
- `bloom_filter_results.png` — experiment figure.

Run the code from this directory so its relative paths to `words.txt` and `typos.json` resolve correctly.

![Bloom filter evaluation results](bloom_filter_results.png)

## Discussion

Bloom-filter membership responses can leak information about a vocabulary: a user can submit likely candidates and observe which ones pass. Increasing the number of hash functions reduced some false positives in this experiment, although it increases computation. Cryptographic hashes also do not prevent this membership-query leakage; they only provide hash values for setting and checking bits.

The Good Suggestion Rate exceeded 85% at approximately 250 million bits with one hash function, between 20 and 30 million bits with two hash functions, and 11 million bits with three hash functions. Allowing more edits expands the candidate space and can increase false positives.
