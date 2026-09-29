# list of objects
class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

p1 = Person('Sonu','male')
p2 = Person('Mou','female')
p3 = Person('Ribhu','male')

L = [p1,p2,p3]

print(L)                                ## In list there save the addresses of objects

for i in L:
    print(i.name, i.gender)