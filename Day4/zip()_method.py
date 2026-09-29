# Write a program to add items of 2 lists index-wise

L1 = [1,4,2,7]
L2 = [3,-1,-2,-3]

L = [i + j for (i , j) in zip(L1, L2)]
print(L)


# --------------------------------------- #

names = ["Sonu", "Ankit", "Rahul"]
scores = [85, 92, 78, 8]

zipped = zip(names, scores)

print(list(zipped))

# The zip() function in Python is used to pair elements
# If the lists are different lengths, zip stops as soon as the shortest list is exhausted.
