# Write a program that can convert an integer to string

number = int(input("Enter the number: "))

digits = '0123456789'
result = ''
while number != 0:
    result = digits[number % 10] + result
    number = number // 10

print(result)
print(type(result))
