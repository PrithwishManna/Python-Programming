class Person:
    def __init__(self,name_input,country_input):
        self.name = name_input
        self.country = country_input

    def greet(self):
        if self.country == 'India':
            print('Sagatam',self.name)
        else:
            print('Hello',self.name) 


P = Person('Subham', 'India')                           ## P is not the object, P contains the address of the object
print(P.country)                                        # How to access attributes
print(P.greet)                                          # How to access methods

## Attribute creation from outside of the class
P.gender = 'male'
print(P.gender)
