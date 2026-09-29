## List Comprehension

# add 1 to 10 numbers to a list
L = [i for i in range(1, 11)]
print(L)

# scalar multiplication on a vector
v = [2,4,5]
s = -2

v1 = [s*i for i in v]
print(v1)

# add squares
v2 = [i ** 2 for i in v]
print(v2)

# Print all numbers divisible by 5 in 1-50
M = [i for i in range(1, 51) if (i % 5) == 0]
print(M)

# find languages which start with letter p
languages = ['java','python','c','html','php']
N = [lan for lan in languages if lan.startswith('p')]
print(N)
