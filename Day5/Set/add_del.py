# Adding items
# Add
S = {1,4,2}
S.add(5)
print(S)

# Update
s1 = {1,32,4}
s1.update([3,5,6])
print(s1)

# Deleting items
# del
s2 = {1,2,0}
print(s2) 
del s2                      # print(s2) => throw an error because s2 doesn't exists after deleting

# discard
S.discard(1)                # It removes particular element from set
print(S)                    # if we do discard(30) => S dosen't change(not error)

# remove
s1.remove(4)                # same as discard
print(s1)                   # if the removal element isn't belong in set then it gives error

# pop
s1.pop()                    # it removes element randomly
print(s1)

# clear
s1.clear()                  # it's clear the elements from the set and create empty set
print(s1)