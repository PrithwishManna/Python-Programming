## Inheritence and its benifits
#### Here in diagram 'Triangle' sign will be present(Direction would be Parent side <-)
# What gets Inherited?
## Constructor, Non-private Attributes, Non private Methods


# Parent
class User:
    def __init__(self):
        self.name = 'Sonu'
        self.gender = 'male'
    def login(self):
        print('login')

# Child
class Student(User):
    def enroll(self):
        print('enroll into the course')

u = User()
s = Student()

print(s.name)
s.login()
s.enroll()