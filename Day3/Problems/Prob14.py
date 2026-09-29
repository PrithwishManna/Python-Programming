# Given two sentences as strings A and B. The task is to return a list of all uncommon words. 
# A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence. 
# Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters.
## Input: s1 = "apple banana mango" , s2 = "banana fruits mango"

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

words1 = s1.split()
words2 = s2.split()

uncommon_words = []

for word in words1:
  if word not in words2:
    uncommon_words.append(word)

for word in words2:
  if word not in words1:
    uncommon_words.append(word)

print(uncommon_words)
