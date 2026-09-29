# We are given a string and we need to reverse words of a given string.
# Input: my name is Sonu

s = input("Enter the string: ")

words = s.split()

reversed_words = words[ : : -1]

result = " ".join(reversed_words)

print(result)
