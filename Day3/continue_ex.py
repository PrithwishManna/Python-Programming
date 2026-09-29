text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

print('\n')


# Alternate

term = input("What would you like to remove: ")
result = ''
for i in text:
    if i != term:
        result += i

print(result)