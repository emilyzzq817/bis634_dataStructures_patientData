# Algorithm Analysis and Performance Measurement

## Development from studio work

The work progressed from small correctness checks for the two supplied sorting functions to timed experiments across chaotic, ordered, and reverse-ordered inputs. The final version separates data generation from timing, adds a log-log benchmark figure, and connects the observed scaling patterns to algorithm selection.

### 2a.

I tested `alg1` and `alg2` with four small lists:

| Input | `alg1` output | `alg2` output |
| --- | --- | --- |
| `[1, 2, 3]` | `[1, 2, 3]` | `[1, 2, 3]` |
| `[3, 2, 1]` | `[1, 2, 3]` | `[1, 2, 3]` |
| `[2, 1, 2]` | `[1, 2, 2]` | `[1, 2, 2]` |
| `[7, -1, 2]` | `[-1, 2, 7]` | `[-1, 2, 7]` |

Both functions sort numbers from smallest to largest. These tests show that they work with an already sorted list, a reversed list, duplicate values, and a negative value.

`alg1` compares neighboring numbers and swaps them if they are in the wrong order. It repeats this process until it can go through the entire list without making a swap.

`alg2` splits the list into smaller lists, sorts them, and joins them back together in order.

### 2b. 

I used `time.perf_counter()` to measure how long each sorting function took for input sizes from about 10 to 1000. I generated each list before starting the timer, so the measured time did not include data generation. I tested small inputs first, then plotted the results on log-log axes.

![Runtime comparison on log-log axes](benchmark.png)

The lines show that running time increases at different rates. On a log-log plot, a steeper line means that time grows faster as the input gets larger. If a line has a slope near 1, making the input 10 times larger would make the time about 10 times longer. With a slope near 2, the time would be about 100 times longer. The smallest inputs run very quickly, so their measured times can vary between runs.

### 2c. 

The input order has a large effect on `alg1`. `data2` is already sorted, so `alg1` checks the list once, makes no swaps, and stops. This is why its line stays low in the middle plot. `data3` is reversed, so many numbers must move across the list. `alg1` needs many passes, and its running time rises quickly. The larger `data1` inputs also require many swaps.

`alg2` splits and merges the list for all three inputs. The original order can change some of its comparisons, but its running time grows at a similar rate in all three plots.

For a small list that is already sorted or nearly sorted, I would consider `alg1` because it can stop after a pass with no swaps. For a large list with an unknown or reversed order, I would choose `alg2`. In my plots, it is much faster on larger `data1` and `data3` inputs and is less affected by input order.
