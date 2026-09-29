## Functiions argument is a function

def func_a() :
    print('inside func_a')               # Because there is no return "some value", it implicitly returns None.

def func_b(z) :                          # z = func_a
    print(' inside func_b')
    return z()                           # z() -> func_a()   # The line return z() effectively becomes return None

print(func_b(func_a))