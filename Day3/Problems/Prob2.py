# Write a Python Program to Find the Sum of the Series till the nth term:

# x + x^2/2 + x^3/3 + ... + x^n/n
# n will be provided by the user

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))

sum = 0

for i in range(1, n + 1):
    term = (x ** i) / i
    sum += term

print(f"The sum of the series for n = {n} is: {sum}")
