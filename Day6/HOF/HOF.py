## Higher Order Function
# In Python, a Higher-Order Function is a function that does at least one of the following:
#  1. Accepts one or more functions as arguments.
#  2. Returns a function as its result.

def loud_greeting(name):
    return f"HELLO {name.upper()}!"

def soft_greeting(name):
    return f"hey {name.lower()}!"

def greet_person(func, name):
    message = func(name)
    print(message)

greet_person(loud_greeting, 'Sonu')
greet_person(soft_greeting, 'PaYeL')
                  