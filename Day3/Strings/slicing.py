#    012345678910
s = 'hello_world'
print(s[0 : 5])
print(s[2 : ])
print(s[ : 9])
print(s[ : ])
print(s[0 : 9 : 2])
print(s[9 : 0 : -2])        # in negative slicing
print(s[ : : -1])           # Reverse string
print(s[-5 : ])             # Print world
print(s[-1 : -6 : -1])      # Print reverse 'world'


s = 'paschim medinipur'
'''s[0] = 'P'       # strings are immutable
print(s)
'''

"""
del s[-1:-5:2]      # strings are immutable
print(s)            # whole string can be deleted but partially not exists
"""