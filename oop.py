class User:
    def log(self):
        print(self)
        # return self

class Teacher(User):
    def log(self):
        print('I\'m a Teacher!')

class Customer(User):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    @property
    def name(self):
        if self._name == None:
            return 'no_name'
        return self._name

    @name.setter
    def name(self, name):
        if type(name) == str:
            self._name = name
        else:
            self._name = None

    @name.deleter
    def name(self):
        del self._name 

    def __str__(self):
        return self.name + ' ' + self.type
    
    def print_all_customers(customers):     # static method
        for customer in customers:
            print(customer)

    def __eq__(self, other):    # without this method memory adresses are compared which always are different
        if self.name == other.name and self.type == other.type:
            return True
        return False

    __repr__ = __str__    # for representation


customers = [Customer('Jonas', 'Gold'), Customer('Jonas', 'Gold'), Customer(123456, 'Diamond')]

Customer.print_all_customers(customers)
print('Memory IDS:', id(customers[0]), id(customers[1]), id(customers[2])) # memory adresses
print(customers[0] == customers[1])
# data = {customers[0]} # TypeError: unhashable type: 'Customer'
print('All customers in a list:', customers)

# del customers[2].name 
# print('All customers after del:', customers) # AttributeError: 'Customer' object has no attribute '_name'

print('LOG from User:')
customers[0].log()

# print('LOG 2 from User:', customers[2].log())

users = [Customer('Petras', 'Bronze'), Customer('Tomas', 'Silver'), Teacher()]

print('Users:')
for user in users:
    user.log()