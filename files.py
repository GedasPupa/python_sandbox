from types import MappingProxyType

# Open a file
myFile = open('my_file.txt', 'w')
# Write to a file
myFile.write('bla bla bla')
myFile.write(' Python and JavaScript')
myFile.write(' and TypeScript')
# Read file
myFile = open('my_file.txt', 'r')
line = myFile.read()
print(line)
# Close file
myFile.close()

# Append to file
myFile = open('my_file.txt', 'a')
myFile.write(' \'Appended text\'')
myFile.close()

# Get some info
print('File name:', myFile.name)
print('Is closed:', myFile.closed)
print('Opening Mode:', myFile.mode)
# print('Buffer:', myFile.buffer)