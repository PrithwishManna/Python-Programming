s1 = {1,3,6,2,7,9,4}
s2 = {2,5,3,0,4,1,6}

# union(|)
a = s1 | s2
print(a)

# intersection(&)
b = s1 & s2
print(b)

# Difference(-)
c = s1 - s2
print(c)
d = s2 - s1
print(d)

# symmetric difference(^)
e = s1 ^ s2                     # (s1 | s2) - (s1 & s2)
print(e)

# membership test
print(1 in s1)
print(7 in s2)

# iteration
for i in a:
    print(i)