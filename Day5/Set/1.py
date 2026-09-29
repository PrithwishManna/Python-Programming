# A set is an unordered collection of items. Every set element is 'unique' and must be 'immutable'
# However, a set itself is mutable. We can add or remove items from it.

# creating empty set
s = set()
print(s)
print(type(s))

#1D and 2D
s1 = {1,2,3}
print(s1)
#s2 = {1,2,{3,4}} / {1,2,[3,4]}           # A set element must be immutable
#print(s2)

#hetro
s3 = {1,'hello', 4.4, True}             # set elements are unique. In python True = 1
print(s3)
s4 = {2,'sonu',3.14,(1,2,3)}            # set is unordered
print(s4)

# using type conversion
s5 = set([1,2,3])
print(s5)

# Duplicates aren't allowed
s6 = {1,2,1,4,6,2,1}
print(s6)