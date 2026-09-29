# Reference valiable hold the objects
# We can create objects without reference variable as well
# An object can have multiple reference variables
# Assigning a new reference variableto an existing object does not create a new object

## Object without a reference
class Person:
    def __init__(self):
        self.name = 'sarthak'
        self.gender = 'chamiya'
# Multiple ref
p = Person()
q = p
print(id(p))
print(id(q))
# change attribute value with the help of 2nd object
print(p.name)
print(q.name)
q.name = 'subham'
print(p.name)
print(q.name)