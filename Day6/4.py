def f(y):
    x = 1                               ## Here x is local variable
    x += 1
    print(x)

x = 5                                   ## And this is Global variable
f(x)
print(x)

## ________....._________

def g(z):
    p += 1                              ## we can't assign the new value to global x in function.

p = 3
g(p)
print(p)