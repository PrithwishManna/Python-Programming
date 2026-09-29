## Constructor Example

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print('Buying a new phone')

class Smartphone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print('Inside smartphone constructor')
    def buy(self):
        print('Buying a new smartphone')

s = Smartphone('Andriod', 4)


#s = Smartphone(120000, "Apple" ,17)
