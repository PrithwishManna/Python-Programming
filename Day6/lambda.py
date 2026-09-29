# print square of 7
a = lambda x: x ** 2
print(a(7))

# x, y -> x + y
b = lambda x, y: x + y
print(b(2,5))

# Check if a string has 'h'
c = lambda s: 'h' in s
print(c('hello'))

# odd or even
d = lambda n: 'even' if n % 2 == 0 else 'odd'
print(d(23))
