import json

myJSON = '{"name": "John", "age": 30}'

# Parse to dict
user = json.loads(myJSON)
user['last_name'] = 'Doe'

print(myJSON)
print(user)

# Parse to JSON
car = {'make': 'ford', 'model': 'mustang', 'year': 1970}
carJSON = json.dumps(car)
print(car)
print(carJSON)