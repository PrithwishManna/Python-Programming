# Given a string. the task is to check if the string is symmetrical or not. 
# A string is said to be symmetrical if both the halves of the string are the same.

s = input("Enter the string: ")             # khokho

mid = len(s) // 2

if len(s) % 2 == 0:
  first, second = s[ : mid], s[mid : ]
else:
  first, second = s[ : mid], s[mid + 1 : ]


if first == second:
  print("The entered string is symmetrical")
else:
  print("The entered string is not symmetrical")