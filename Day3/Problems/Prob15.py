# Find a location of a word in a given sentence.
## s = I am a boy
## find = boy

s = input("Enter the string: ")
find = input("Enter the word to find: ")

words = s.split()

for i in range(len(words)):
  if words[i] == find:
    print(f"Location of the word is {i}")
    break
else:
  print("Word not found")
  