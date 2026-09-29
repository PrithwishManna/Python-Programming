## Multiply Adjacent elements (both side) and take sum of right and left side multiplication result.

tup = (1, 5, 7, 8, 10)

res = tuple(
    (tup[i] * tup[i - 1] if i > 0 else 0) +
    (tup[i] * tup[i + 1] if i < len(tup) - 1 else 0)
    for i in range(len(tup))
)

print(res)
