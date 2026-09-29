### reduce: combines all items into one single value (N inputs → 1 output).
## reduce is not a built-in global function in Python 3. We must import it from the functools module.

# sum of all item

import functools
L = [1,2,3,4,5,9]
a = functools.reduce(lambda x,y: x + y, L)
print(a)


# find min
M = [7,17,89,3,56,6,30]
b = functools.reduce(lambda x,y: x if x < y else y, M)
print(b)
