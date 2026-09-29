# Write a program that can remove all the duplicate characters from a string. User will provide the input.
## Input = programming

s = input("Enter the string: ")

result = ""

for ch in s:
  if ch not in result:
    result += ch

print(result)
