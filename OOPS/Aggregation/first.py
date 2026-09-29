## Aggregation doesn't access private attributes
#### Here in diagram 'Rohmbus' sign will be present

class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    def print_address(self):
        print(self.address._Address__city,self.address.pin,self.address.District)
    def edit_profile(self,new_name,new_city,new_pin,new_district):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_district)

class Address:
    def __init__(self,city,pin,District):
        self.__city = city
        self.pin = pin
        self.District = District
    def get_city(self):
        return self.__city
    def edit_address(self,new_city,new_pin,new_district):
        self.__city = new_city
        self.pin = new_pin
        self.District  = new_district


add1 = Address('Ghatal',721212,'West Bengal')
cust1 = Customer('Arup','Male',add1)

cust1.print_address()

cust1.edit_profile('Himanshu','Kishanganj',450083,'Murshidabad')
cust1.print_address()