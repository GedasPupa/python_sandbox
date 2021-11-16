# Create a function
def myFunc():
    print('Just hellooo to everybody') # must be defined before calling

def sayHello(name = 'Andrius'): # assigning default value to a parameter
    print(f'Hello dear {name}')
    myFunc()

# Call a function
sayHello('Tomas')
sayHello()

# Return values
def sum(num1, num2):
    return num1 + num2
print(sum(2, 7))

# A lambda function is a small anonymous function
# A lambda funtion can take any number of arguments, but can only have one expression. 
# They are very similar to JS arrow functions.

getSum = lambda n1, n2 : n1 + n2
print(getSum(1,6))