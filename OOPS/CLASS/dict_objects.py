# dictionary of objects

class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

p1 = Person('Sonu','male')
p2 = Person('Mou','female')
p3 = Person('Ribhu','male')

d = {'p1':p1, 'p2':p2, 'p3':p3}

for i in d:
    print(i)                                    ## print keys
    print(d[i])                                 ## print addresses of keys
    print(d[i].name, d[i].gender)               ## print class objects