### In python we use a function as a variable, as a data type
### just like first class in Python

def square(x):
    return x ** 2

L = [1,3,2,5,square]
print(L)
print(L[-1](3))

type(square)
id(square)

a = square
print(a(4))