# len/min/max/sorted
L = [2,1,5,4,0,7,2,5,2]

print(len(L))
print(min(L))
print(max(L))
print(sorted(L))                    # temporary method           

print(sorted(L,reverse=True))

#L.sort()                           # permanently sorting the list
#print(L)

# count
print(L.count(2))                   # find out how many times a specific value appears in a list

# index
print(L.index(7))
print(L.index(5))                   # index() only gives you the position of the very first one it finds

print(L.index(2, 1))                # Find the first '2' starting the search from index 1

# reverse
L.reverse()                         # permanently reverses the list
print(L) 

# copy
L1 = [1,2,3,4]
print(L1)
print(id(L1))

L2 = L1.copy()                      # Shallow copy
print(L2)
print(id(L2))
