N1 = int(input("Enter first number: "))
N2 = int(input("Enter second number: "))
N3 = int(input("Enter third number: "))

largest_number = N1

if N2 > largest_number:
	largest_number = N2

if N3 > largest_number:
	largest_number = N3

print("The largest number is:", largest_number)

"""
largest_number = max(N1, N2, N3)
print("The largest number is:", largest_number)
"""
