#  *args
### allows us to pass a variable number of non-keyword arguments to a function

def multiply(*args):                        ## *args handle many many arguments
    product = 1

    for i in args:
        product *= i

    return product

x = multiply(1,2,3,4,5,6)
print(x)

#  **kwargs
### allows us to pass any number of keyword arguments.
### keyword arguments mean that they contain a key-value pair, like a Python dictionary

def display(**kwargs):                                   ## Instead of 'kwargs' we can write anything like 'sonu'
    for (key,value) in kwargs.items():
        print(key,'->',value)

display(India = 'Delhi', USA = 'New York', Japan = 'Tokyo', China = 'Shang-Hai')

## order of the arguments matter(normal -> *args →> **kwargs)
## The words "args" and "kwargs" are only a convention, we can use any name of our choice