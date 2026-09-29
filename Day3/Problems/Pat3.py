# Write a program to use for loop to print the following reverse number pattern.

# 5 4 3 2 1
#  4 3 2 1
#   3 2 1
#    2 1
#     1

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for x in range(rows - i):     # For front spaces
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j , end=' ')
    print()