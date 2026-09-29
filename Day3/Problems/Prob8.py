# Append second string in the middle of first string

s1 = input("Enter a string in which's middle portion add another string: ")
s2 = input("Enter another string: ")

index = len(s1) // 2
new_string = s1[:index] + s2 + s1[index:]

print(new_string)