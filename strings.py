name = 'Brad'
age = 39

# Concatenate
# print('Hello my name is ' + name + ' and I am ' + str(age) + '.')

# Arguments by position
# print('Hello my name is {nnaammee} and I am {age} years old.'.format(nnaammee=name, age=age))

# F-Strings (3.6+)
print(f'Hello my name is {name} and I am {age} y.o. - not too old for learning Python! :)')

#  String methods

alpha = 'aabBBBCccZ'
s = '123333helloworlD'
n = '11101'

print(s.capitalize())
print('find(\'o\')', s.find('o'))
print('count(\'l\'): ', s.count('l'))
print('length of s: ', len(s))
print('islower()???', s.islower())
print('is alpha numeric?', s.isalnum())
print('isalpha()? ', alpha.isalpha())
print('endwith(\'a\')', s.endswith('a'))
print('isdigit()', n.isdigit())
print('split(): ', s.split())
print('rsplit(): ', s.rsplit())
print(s.replace('123', 'Hello hello, '))