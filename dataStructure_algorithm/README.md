### 2a.

I tested `alg1` and `alg2` with four small lists:
| Input | `alg1` output | `alg2` output |
| -- | -- | -- |
| `[1, 2, 3]` | `[1, 2, 3]` | `[1, 2, 3]` |
| `[3, 2, 1]` | `[1, 2, 3]` | `[1, 2, 3]` |
| `[2, 1, 2]` | `[1, 2, 2]` | `[1, 2, 2]` |
| `[7, -1, 2]` | `[-1, 2, 7]` | `[-1, 2, 7]` |

Both functions sort the input in ascending order. The tests let them handle an sorted list, a reversed list, duplicate values, and a negative value.

`alg1` looks at two neighboring numbers at a time and swaps them if they are in the wrong order. It goes through the list again until it can make a full pass without swapping anything. `alg2` splits the list into smaller lists. It sorts those lists, then joins them together in order.
