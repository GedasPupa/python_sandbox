# OOP - 2

class PlayerCharacter:
    # Class Object Attribute
    membership = True # Static

    def __init__(self, name='anonymous', age=0):
        if self.membership and age > 18:        # or: if PlayerCharacter.membership:
            self.name = name # attributes
            self.age = age
        else:
            return ValueError

    def __str__(self):
        return self.name + ' ' + str(self.age)
    
    __repr__ = __str__
    
    def run(self):
        print(self.name + ' running')
        return 'done'

    @classmethod
    def sum(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod       # has no access to 'cls'
    def sum2(num1, num2):
        return num1 + num2

pl1 = PlayerCharacter('John', 33)
pl2 = PlayerCharacter('Jonas', 21)

print(pl1.run())
# print(pl2)
print(PlayerCharacter.sum(33, 5).sum(22, 1))


class User:
    def __init__(self, email):
        self.email = email
    def log_in(self):
        print('logged in!')
    def attack(self):
        print('Do nothing..')


class Wizzard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email) # or just (when without multiple inheritance): super.__init__(email)
        self.name = name
        self.power = power

    def __str__(self):
        return f'{self.name} / {self.power} / {self.email}'
    
    __repr__ = __str__
    
    def attack(self):
        print(f'Wizzard {self.name} attacking with power {self.power}!')

class Archer(User):
    def __init__(self, name, arrows, email):
        User.__init__(self, email) # or just (when without multiple inheritance): super.__init__(email)
        self.name = name
        self.arrows = arrows
        self.my_dict = {
            'kingdom': 'UK',
            'magic': True
        }

    def attack(self):
        User.attack(self) # or: super().attack()
        print(f'Archer {self.name} attacking with {self.arrows} arrows!')
    
    def __str__(self):
        return f'{self.name} / {self.arrows} / {self.email}'
    
    __repr__ = __str__

    def __call__(self):
        return f'{self.name} - yesss, I\'m called!'

    def __len__(self):
        return 2121212121

    def __getitem__(self, i):
        return self.my_dict[i]
    
class HybridBorg(Archer, Wizzard): # MRO - Method Resolution Order
    def __init__(self, name, power, arrows, email):
        Wizzard.__init__(self, name, power, email)
        Archer.__init__(self, name, arrows, email)

w1 = Wizzard('Burtininkas', 10, 'wiz@wiz.com')
w1.log_in()
w1.attack()

a1 = Archer('Lankininkas', 21, 'ar@ar.com')
a1.log_in()
a1.attack()

def char_attack(char):
    char.attack()

char_attack(w1)
char_attack(a1)

for c in [a1, w1]:
    c.attack()

print(a1, '//', w1)


# introspection - determine the type of an object at runtime
print(dir(a1))
print(a1()) # __call__()
print(len(a1)) # __len__()
print('MAGiC:', a1['magic'], 'KingDom:', a1['kingdom']) # __getitem__(self, i)

class SuperList(list):
    def __len__(self):
        return 1000000

s_list1 = SuperList()
s_list1.append(21)

print(len(s_list1), s_list1[0])
print(issubclass(SuperList, list))
print(issubclass(list, object))

hb1 = HybridBorg('HHH', 50, 300, 'ggg')
print(hb1())
print(HybridBorg.mro()) # MRO - Method Resolution Order: [<class '__main__.HybridBorg'>, <class '__main__.Archer'>, <class '__main__.Wizzard'>, <class '__main__.User'>, <class 'object'>]
print(hb1.attack()) # runs Archer.attack() first:
# cls A, cls B(A), cls C(A), cls D(B, C):
#    A
#   / \
#  /   \
# B --> C
#  \   /
#   \ /
#    D

class X: pass 
class Y: pass 
class Z: pass 
class A(X, Y): pass 
class B(Y, Z): pass 
class M(B, A, Z): pass # try: class M(A, B, Z): pass 

print('MMM mro():', M.mro())

print(hb1.power)
print(hb1.arrows)
print('Magic:', hb1['magic'])


# print(isinstance(a1, Archer)) # False
# print(isinstance(a1, Wizzard)) # False
# print(isinstance(a1, User)) # True
# print(isinstance(w1, object)) # True
# print('--- issubclass:')
# print(issubclass(Archer, User)) # True
# print(issubclass(Wizzard, User)) # True




# class BigObject:
#     pass
# obj1 = BigObject()

# print(type(None))
# print(type(True))
# print(type(5))
# print(type(0.21))
# print(type('string'))
# print(type([]))
# print(type(()))
# print(type({}))
# print(type(BigObject))
# print(type(obj1))

