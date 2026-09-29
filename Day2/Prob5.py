# Write a program to use the loop to find the factorial of a given number.
num = int(input("Enter an integer : "))
number = 1

if num > 0:
    for i in range(1, num + 1):
        number *= i
    print(f"factorial of {num} : {num}! =", number)
elif num == 0:
    print(f"{num}! = {num}")
else:
    print("Enter a positive integer!")