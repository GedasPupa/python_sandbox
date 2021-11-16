# TUPLE is a collection which is ordered and unchangable. Allows duplicate members.
# Create Tuple

fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('aplle', 'orange', 'banana'))
fruits3 = ('Apple',) # single value needs trailing comma
print(fruits, fruits2)
print(fruits3, type(fruits3))
print(fruits[1])
# fruits[0] = 'Banana'  # TypeError - you can't change the value
del fruits2
# print(fruits2)    # NameError - 'fruits2' is not defined.
print(len(fruits))

# A SET is a collection which is unordered and unindexed. No duplicate memebers.
# Create Set
fruits_set = {'Apple', 'Orange', 'Kiwi'}

# Check if smthg in set
print('Orange' in fruits_set) # --> True

# Add to Set
fruits_set.add('Grape')
# Add the same
fruits_set.add('Apple')
print('added the same (\'Apple\')???', fruits_set)

# Remove from set
fruits_set.remove('Apple')
print(fruits_set)

# Clear Set
fruits_set.clear()
# del fruits_set # deletes set
print('CLEAR SET: ', fruits_set)