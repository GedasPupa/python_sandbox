# define enumerations using the Enum base class
from enum import Enum, unique, auto

# @unique # unique decorator doesn't let to have a duplicate values!
class Fruits(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()

    RED_DELICIOUS = 1 # values can be the same, then no @unique
    # APPLE = 6 # it is not valid to have duplicate name

def main_0():
    print(Fruits.APPLE)
    print(type(Fruits.APPLE))
    print(repr(Fruits.APPLE))

    # enums have name and value properties
    print(Fruits.APPLE.name, Fruits.APPLE.value)
    print(Fruits.PEAR.value)

    # enums are hashable - can be uses as keys
    myFruits = {}
    myFruits[Fruits.BANANA] = 'ohoho megstu bananus'
    print(myFruits)
    print(myFruits[Fruits.BANANA])

    
# Class string functions: __str__(), __repr__(), __bytes__(), __format__()
class Person:
    def __init__(self):
        self.name = 'Gedas'
        self.surname = 'Pupa'
        self.age = 21
    
    def __repr__(self):
        return '<class Person> {name:' + self.name + ', surname: ' + self.surname + ', age: ' + str(self.age) +'}'

    def __str__(self):
        return f'\'{self.name} {self.surname} is {self.age}\''

    def __bytes__(self):
        val = 'Person:{0}:{1}:{2}'.format(
            self.name, self.surname, self.age
        )
        return bytes(val.encode('utf-8'))


# Class Attribute functions: 
# __getattribute__(self, attr)-called every time unconditionally attribute name is requested 
# __getattr__(self, attr)-called only when requested attribute name can't be found in the object
# __setattr__(self, attr, val), __delattr__(self), __dir__(self)

class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    def __getattr__(self, attr):
        if attr == 'rgbcolor':
            return (self.red, self.green, self.blue)
        elif attr == 'hexcolor':
            return '#{0:02x}{1:02x}{2:02x}'.format(
                self.red, self.green, self.blue
            )
        else:
            raise AttributeError

    def __setattr__(self, attr, val):
        if attr == 'rgbcolor':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)
    
    def __dir__(self):
        return ('red', 'green', 'blue', 'rgbcolor', 'hexcolor')

# Object operations: object.__add__(self, other)[self+other], __sub__(s,o)-, __mul__(s,o)*,
# __div__(s,o)/, __floordiv__(s,o)//, __pow__(s,o)**, __and__(s,o)&, __or__(s,o)|
# __iadd__(s,o)+=, __isub__(s,o)-=, __imul__(s,o)*=, __itruediv__(s,o)/=, 
# __ifloordiv__(s,o)//=, __ipow__(s,o)**=, __iand__(s,o)&=, __ior__(s,o)|=

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<Point x:{self.x}, y:{self.y}>'

    def __add__(self, other):
        # (creates new point):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


# Class Comparison Operators:
# __gt__(serl,other)>, __ge__()>=, __lt__()<, __le__()<=
# __eq__()==, __ne__()!=

class Employee():
    def __init__(self, name, seniority, yrsService):
        self.name = name
        self.seniority = seniority
        self.yrsService = yrsService

    def __ge__(self, other):
        if self.seniority == other.seniority:
            return self.yrsService >= other.yrsService
        return self.seniority >= other.seniority

    def __gt__(self, other):
        if self.seniority == other.seniority:
            return self.yrsService > other.yrsService
        return self.seniority > other.seniority
    
    def __lt__(self, other):
        if self.seniority == other.seniority:
            return self.yrsService < other.yrsService
        return self.seniority < other.seniority

    def __le__(self, other):
        if self.seniority == other.seniority:
            return self.yrsService <= other.yrsService
        return self.seniority <= other.seniority


def main_1():
    p1 = Person()
    print(p1)
    print(repr(p1))
    print(str(p1))
    print('Formated: {0}'.format(p1))
    print(bytes(p1))

def main_2():
    cl1 = myColor()
    print(cl1.rgbcolor)
    print(cl1.hexcolor)

    cl1.rgbcolor = (125, 80, 140)
    print(cl1.rgbcolor)
    print(cl1.hexcolor)

    print(dir(cl1))

def main_3():
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    p3 = Point(2, 2)
    print(p1 + p2 + p3)
    print(p2 - p1 - p3)
    print(p1, p2, p3)

    # in-place addition: object.__iadd__(self, other)
    p1 += p2
    p1 += p3
    print(p1, p2, p3)

def main_4():
    emps = []
    emps.append(Employee('Tom', 5, 12))
    emps.append(Employee('John', 4, 7))
    emps.append(Employee('Anna', 5, 11))
    emps.append(Employee('Peter', 6, 21))
    emps = sorted(emps, reverse=True) # lets to sort by seniority / yrsService
    for e in emps:
        print(e.name)

if __name__ == '__main__':
    # main_0()
    # main_1()
    # main_2()
    # main_3()
    main_4()