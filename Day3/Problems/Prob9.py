# Given string contains a combination of the lower and upper case letters. 
# Write a program to arrange the characters of a string so that all lowercase letters should come first.

input_str = input("Eneter a string(upper_lower_upper): ")

lower = ""
upper = ""

for char in input_str:
    if char.islower():
        lower += char
    else:
        upper += char

result = lower + upper
print(result)