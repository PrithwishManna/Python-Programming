# need for static vars

class Atm:

    counter = 1

    # constructor(special function) ->It will run explicitly without calling whenever we create a new object of the class
    def __init__(self):
        self.pin = ''
        self.__balance = 0                    ## self.balance -> self.__balance (private)

        self.cid = Atm.counter
        Atm.counter += 1 

        self.menu()                         # print('This will execute automatically')
    def get_balance(self):
        return self.__balance
    
# static method
    def get_counter():
        return Atm.__counter

    def set_balance(self,new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print('Tumse na hoga')
        


    def menu(self):
        user_input = input("""
        Hi How can I help you?
        1.Press 1 to create pin
        2.Press 2 to change pin
        3.Press 3 to check balance
        4.Press 4 to withdraw
        5.Anything else to exit
        """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':             # In Python, you cannot leave an if or elif block empty (or containing only comments). The interpreter expects at least one line of executable code.
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input('Ent1er your pin: ')
        self.pin = user_pin

        user_balance = int(input('Enter your balance: '))
        self.__balance = user_balance

        print('Pin created successfully')
        self.menu()
    
    def change_pin(self):
        old_pin = input('Enter your old pin: ')
        if old_pin == self.pin:                                       #Let him change the pin
            new_pin = input('Enter a new pin: ')
            self.pin = new_pin
            print('Pin change successfully')
            self.menu()
        else:
            print('You entered the wrong pin')
            print('Try again')
            self.change_pin()

    def check_balance(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.pin:
            print('Your balance is: ', self.__balance)
        else:
            print('You entered the wrong pin')
            print('We cannot show you the balance')
        self.menu()

    def withdraw(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.pin:
            amount = int(input('Enter the amount: '))
            if amount <= self.__balance:
                self.__balance -= amount
                print('Withdrawl Successfully')
                print('Your balance is now: ', self.__balance)
            else:
                print('Insufficient balance')
        else:
            print('You entered the wrong pin')
            print('We cannot withdraw the money')
        self.menu()

obj = Atm()               # object-name = class-name                  # print(type(Atm()))
obj.__balance = 'chdsbch'

c1 = Atm() 
c2 = Atm() 
c3 = Atm() 

print(c1)