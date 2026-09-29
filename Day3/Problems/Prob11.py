# Removal of all characters from a string except integers.

str1 = 'I am 22 years and 10 months old'
List = []

for char in str1:
    if char.isdigit():
        List.append(char)

sr = int("".join(List))
print(sr)
print(type(sr))