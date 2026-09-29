user_word = input("Enter a word: ").upper() 

consonants_only = ""

VOWELS = "AEIOU"

for letter in user_word:
    if letter in VOWELS:
        continue
    consonants_only += letter

consonants_only = consonants_only.lower()

print("Filtered word:", consonants_only)