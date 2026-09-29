## Do the square of elements of any given list

#def square(x):
#    return x ** 2

def transform(func, L):
    output = []
    for i in L:
        output.append(func(i))

    print(f"After square list becomes L = {output}")

L = [1,2,3,6,5,7,4]
transform(lambda x: x ** 2, L)


## map function                 # It follows the concept of mapping inputs to outputs.
# The map() function is a built-in Python tool used to apply a specific function to   
# every item in an iterable (like a list or tuple) without writing a generic for loop.

a = map(lambda x: x ** 2, [1,2,3,6,5,7,4])
print(a)
print(list(a))

