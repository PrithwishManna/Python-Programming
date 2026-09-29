# child can't access private members of the class

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def show(self):
        print(self.__price)

class Smartphone(Phone):
    def check(self):
        print(self.__price)

s = Smartphone(40000,'Apple',13)
print(s.brand)
s.show()

#s.check()                      ## child can't have access of private members of parent
