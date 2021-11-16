# A Dictionary is a collection which is unordered, changable and indexed. No duplicate members.

# Create dict

person = {
    'first_name': 'Jonas',
    'last_name': 'Jonaitis',
    'age': 21
}

print(person, type(person))

person2 = dict(first_name='Onute', last_name='Onaite')

print(person2)
print(person['first_name'])
print(person.get('last_name'))
person['phone'] = '8 666 11111'
print(person['phone'])

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person3 = person2.copy() 
person3['city'] = 'Vilnius'
print('person2:', person2)
print('person3', person3)

# Remove item
del(person['phone'])
person.pop('age')
print('person without phone and age:', person)

# Clear
person.clear()
print(person)

# Get length
print(len(person), len(person2), len(person3))

# List of dict
people = [
    {'name': 'Andrius', 'age': 66},
    {'name': 'Tomas', 'age': 21}
]

print('people[0]:', people[0])
print(people[1]['name'])