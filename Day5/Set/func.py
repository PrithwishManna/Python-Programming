# len/sum/max/min/sorted
s = {1,5,6,2,0,4,5,8}
print(len(s))

print(sum(s))

print(max(s))

print(min(s))

print(sorted(s))                # it gives ans in 'list' in ascending order
print(sorted(s,reverse=True))

# union/update
r = {2,1,4,7,9,0,3,8}                 
print(r.union(s))               # it creates a new set
print(5 in r)

r.update(s)                     # update function change r permanently
print(r)
print(5 in r)

# intersection/intersection_update
print(r.intersection(s))
print(9 in r)

r.intersection_update(s)        # intersection_update function change r permanently
print(r)
print(9 in r)

# difference/difference_update
a = {2,4,6,8,0,1}
b = {3,2,6,7,9,1}
print(a.difference(b))
print(2 in a)

a.difference_update(b)        # difference_update function change r permanently
print(a)
print(2 in a)

# symmetric_difference/symmetric_difference_update
a1 = {2,4,6,8,0,1}
b1 = {3,2,6,7,9,1}
print(a1.symmetric_difference(b1))
print(2 in a1)

a1.symmetric_difference_update(b1)        # symmetric_difference_update function change r permanently
print(a1)
print(2 in a1)

# isdisjoint/issubset/issuperset
print(a1.isdisjoint(b1))

x = {1,2,4}
y = {1,2,0,4,3,6}

print(x.issubset(y))

print(y.issuperset(x))