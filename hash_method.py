class Data:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        return self.a == other.a
        # return self is other


    def __hash__(self):
        return hash((self.a))
    # def __str__(self):
    #     return str(self.a)
    # __repr__ = __str__

data = Data("100")
data2 = Data("100")
res = hash(data)
res2 = hash(data2)
print(data == data2, res == res2, res, res2, 'data:', data, data2)

class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        
    def __hash__(self):
        return hash((self.name, self.age, self.sex))

ann = Person('Ann', 23, 'w')
ann_2 = Person('Ann', 23, 'w')
alice = Person('Alice', 33, 'w')
# print(hash(ann))
# print(hash(ann_2))
# print(hash(alice))

t1 = (1, 2)
t2 = (1, 2)
# print(t2 is t1) # ??? why in console different
# print(t1 == t2)
# print(hash(t1) == hash(t2))