def hello():
    print('hello')

greet = hello

del hello
# hello() # error

print(greet) 
print(greet())

# Higher Order Function - HOC
def pasisveikink(func): # HOC - accepts func as a parameter
    func()

def pasisveikink2():    # HOC - or returns a function
    def func():
        print('labas2')
    return func

def labas():
    print('labas')

pasisveikink(labas)
pasisveikink2()()

# Decorator

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print(args, kwargs)
        if args[0] == 3: print(f'labas {args[0] + args[1] - 0.5}')
        else: print(f'labas {args[0] - 1}')
        func(*args, **kwargs)
        print(f'labas {args[0] + 1}')
        if len(kwargs.values()) > 0: 
            for i in kwargs.values(): 
                print('kwarg value:', i)
    return wrap_func



@my_decorator
def labas3(greeting=3, g2=2, emoji=":)"):
    print('llaabbaass ' + emoji + ' ' + str(greeting))

labas3(3, 12, emoji=':(')
labas3(6, 18)

def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    print(kwargs)
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real ", b="Python ", c="Is ", d="Great", e="!"))

from time import time



def performance(func):
    def w_f(*args, **kwargs):
        a = time()
        result = func(*args, **kwargs)
        b = time()
        print('It tooked: ', b-a)
        return result
    return w_f

@performance
def long_time():
    sum = 0
    for i in range(10000000):
        sum += i+100000000000000000000000000000000000000000000000000000000000000000
    return sum

print(long_time())
