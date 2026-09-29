# Given a string create short form of the string from Initial character. Short form should be capitalised.

text = input("Enter the string: ")

words = text.split()

short_form = ""

for word in words:
    if word != 'of' and word != 'and' and word != 'to' and word != 'in':
        initial = word[0]

        short_form += initial.upper()

print(f"Output: {short_form}")