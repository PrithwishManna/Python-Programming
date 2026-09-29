# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

n = int(input("Enter an integer: "))

L = []
S = ''
sum = 0

for i in range(n):
    S = S + '2'
    L.append(S)
    sum += int(S)

print(f"sum of the series {'+'.join(L)} is:", sum)