# menu driven calculator
fnum = int(input('Enter the 1st number: '))
snum = int(input('Enter the 2nd number: '))

op = input('Enter any operation : ')

if op == '+':
    print(fnum + snum)
elif op == '-':
    print(fnum - snum)
elif op == '*':
    print(fnum * snum)
else:
    print(fnum / snum)