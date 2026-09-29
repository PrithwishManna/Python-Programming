# Create 2 lists from a given list where
# 1st list will contain all the odd numbers from the original list and
# the 2nd one will contain all the even numbers

L = [1,2,3,4,5,6,8,7]

L1 = [i for i in L if (i % 2) != 0]
L2 = [j for j in L if (j % 2) == 0]

print(L1)
print(L2)



# How to take list as input from user

size = int(input("Enter the size of list: "))
M = []

for i in range(size):
    a = int(input("Enter the element: "))
    M.append(a)

print(M)
