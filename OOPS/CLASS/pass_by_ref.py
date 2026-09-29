## Pass by reference
### user defined all objects are mutable

class Person:
    
    def __init__(self,nam,gen):
        self.name = nam
        self.gender = gen

# outside the class -> function
def greet(per):
    print(id(per))                                                  ## here
    print('Hi my name is',per.name,'and I am a',per.gender)
    p1 = Person('Pradip','Tharki')
    return p1

p = Person('Prithwish', 'male')
print(id(p))                                                        ## there and here both have same address 
x = greet(p)
print(x.name)
print(x.gender)
