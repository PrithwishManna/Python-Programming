# Write a program to count the number of words in a string without split()

s = input("Enter the string: ")
L = []
temp = ''

for i in s:
    if i != ' ':
        temp = temp + i
    else:
        L.append(temp)
        temp = ''

L.append(temp)
print(L)
