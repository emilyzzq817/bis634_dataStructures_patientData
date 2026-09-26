def alg1(data):
    data = list(data)
    changes = True
    while changes:
        changes = False
        for i in range(len(data) - 1):
            if data[i + 1] < data[i]:
                data[i], data[i + 1] = data[i + 1], data[i]
                changes = True
    return data


def alg2(data):
    if len(data) <= 1:
        return data
    else:
        split = len(data) // 2
        left = iter(alg2(data[:split]))
        right = iter(alg2(data[split:]))
        result = []
        left_top = next(left)
        right_top = next(right)
        while True:
            if left_top < right_top:
                result.append(left_top)
                try:
                    left_top = next(left)
                except StopIteration:
                    return result + [right_top] + list(right)
            else:
                result.append(right_top)
                try:
                    right_top = next(right)
                except StopIteration:
                    return result + [left_top] + list(left)

import numpy as np


def data1(n, sigma=10, rho=28, beta=8 / 3, dt=0.01, x=1, y=1, z=1):
    state = np.array([x, y, z], dtype=float)
    result = []
    for _ in range(n):
        x, y, z = state
        state += dt * np.array(
            [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]
        )
        result.append(float(state[0] + 30))
    return result


def data2(n):
    return list(range(n))


def data3(n):
    return list(range(n, 0, -1))


test_cases = [
    [1, 2, 3],
    [3, 2, 1],
    [2, 1, 2],
    [7, -1, 2],
]

for values in test_cases:
    print(f"Input: {values}")
    print(f"alg1:  {alg1(values)}")
    print(f"alg2:  {alg2(values)}")