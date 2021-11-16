# Create list
numbers = [1,2,3]
# Create with constructor
numbers1 = list((1,2,3))

fruits = ['orange', 'apple', 'kiwi']
fruits.append('banana')
fruits.insert(1, 'chocolate')
fruits.remove('apple')
fruits.pop(0)
# fruits.reverse()
# fruits.sort()
fruits.sort(reverse=True)


print('length: ', len(fruits))
for f in fruits:
    print(f)

