## Exercise 2a: Functionality and Mechanics

I tested `alg1` and `alg2` with four small lists:

| Input | `alg1` output | `alg2` output |
| -- | -- | -- |
| `[1, 2, 3]` | `[1, 2, 3]` | `[1, 2, 3]` |
| `[3, 2, 1]` | `[1, 2, 3]` | `[1, 2, 3]` |
| `[2, 1, 2]` | `[1, 2, 2]` | `[1, 2, 2]` |
| `[7, -1, 2]` | `[-1, 2, 7]` | `[-1, 2, 7]` |

Both functions sort the input in ascending order. The tests show that they handle an already sorted list, a reversed list, duplicate values, and a negative value.

`alg1` repeatedly compares neighboring elements and swaps them when they are out of order. It continues making passes through the list until a full pass requires no swaps. This is bubble sort.

`alg2` splits the list into smaller parts, sorts those parts, and combines them by selecting the smaller next value from each part. This is merge sort.
