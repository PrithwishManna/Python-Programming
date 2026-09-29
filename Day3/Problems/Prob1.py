# Calculate 1/1! + 2/2! + 3/3! + ...

n = int(input("Enter an integer: "))

sum = 0
fact = 1
for i in range(1, n + 1):
    fact *= i
    sum += i / fact

print(f"Your sum of the sequence = {sum}")