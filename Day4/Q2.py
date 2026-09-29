# Write a program to merge 2 list without using the + operator
L1 = [1,2,3]
L2 = [5,6,7]

L1.extend(L2)
print(L1)



# Write a program to replace an item with a different item if found in the list
# replace 3 with 300
L = [1,2,3,4,5,3]
l = []
for i in L:
    if i == 3:
        l.append(300)
    else:
        l.append(i)

print(l)


# alternate
list = [300 if i == 3 else i for i in L]
print(list)