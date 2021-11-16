# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    def greeting(self):
        return f'Hi, my name is {self.name} and I am {self.age}.'
    def birthday(self):
        self.age += 1

# Extend Class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance
    def greeting(self):
        return f'Hi, my name is {self.name} and I am {self.age}. My balance is {self.balance}.'       



# Init User object
brad = User('Brad Traversey', 'ggg@ggg.com', 21)
print(brad.name, 'Type:', type(brad))
print(brad.greeting())
brad.birthday()
print(brad.greeting())

# Init Customer object
janet = Customer('Janet Johnson', 'j@j.com', 27)
janet.set_balance(20.21)
print('Janet balance:', janet.balance)
print(janet.greeting())