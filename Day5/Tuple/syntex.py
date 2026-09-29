# tuple unpacking

a,b,c = (2,5,8)
print(a*b+c)

#swap
p = 4
q = 5
p, q = q, p

print(p, q)

# advanced
x, y, *others = (2, 4, 1, 3, 9)             # here others is variable
print(x, y)
print(others)

# zipping tuples
k = (7, 4, 0, 1)
l = (3, 2, 8, 5)

print(zip(k,l))                             # convert in zip object

print(list(zip(k,l)))                       # List of tuples

print(tuple(zip(k,l)))                      # 2D tuple