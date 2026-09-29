# Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers

num1 = int(input("Enter a positive integer: "))
num2 = int(input("Enter a positive integer: "))

a = num1
b = num2

while b > 0:                    # while min(a, b) > 0:
    remainder = a % b           #   remainder = max(a, b) % min(a, b)
    a = b
    b = remainder

hcf = a

lcm = (num1 * num2) // hcf

print(f"HCF is: {hcf}")
print(f"LCM is: {lcm}")
    