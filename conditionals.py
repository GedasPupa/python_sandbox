x = 1
y = 21

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equale to {y}')
else:
    print(f'{y} is greater than {x}')

# Nested conditionals
if x>5:
    if x<100:
        print(f'{x} is greate than 5 and less than 100')
    else:
        print(f'{x} is greater than 5 but NOT less than 100')
else:
    print(f'{x} is less than 5')

if x>5 and x<100:
    print(f'{x} is greater than 5 AND less than 100')
elif x>5 or x<100:
    print(f'{x} is greater than 5 OR less than 100')

if not(x>5) and x<100:
    print(f'{x} is not greater than 5 and less than 100')

# Membership operators (in, not in)
numbers = [1,2,3,4,5]
if x in numbers:
    print('x is in numbers:', x not in numbers, ' - What a LIE!')

# Identity operators (is, is not). Compare the objects, not if they are equal, but if they
# are actually the same object, with the same memory location.

if x is not y:
    print(f'{x} is not in y')
    print(f'but {x} is in numbers:', x is numbers[0], ' index: ', numbers.index(x))

person = {
    'name': 'John'
}
person2 = person
person3 = person.copy()
print('person is person2?', person is person2)
print('person is person3?', person is person3)