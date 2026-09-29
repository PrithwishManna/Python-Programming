# print all prime numbers in b\w any range

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print(f"prime numbers b\w {lower}-{upper}: ")
for i in range(lower, upper + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=' ')
        