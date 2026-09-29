# Program - Find the sum of a 3 digit number entered by the user
num = int(input("Enter a digit number: "))    # 549

a = num % 10        # 9 

num //= 10          

b = num % 10        # 4

c = num // 10       # 5

total = a + b + c
print(total)