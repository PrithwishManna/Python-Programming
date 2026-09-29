# Check Palindrome(abba, malayalam, racecar)

s = input("Enter the string: ")

flag = True

for i in range(len(s)//2):
    if s[i] != s[len(s) - i - 1]:
        flag = False
        print("This is not a Palindrom")
        break

if flag:
    print('This is a Palindrom')