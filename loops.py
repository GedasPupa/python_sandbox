people = ['jonas', 'tomas', 'andrius', 'antanas']

# Break
# for p in people:
#     print(f'current person: {p}')
#     if p == 'tomas':
#         break

# Continue
# for p in people:
#     if p == 'tomas':
#         continue
#     print(f'current person: {p}')

# Range
for i in range(len(people) - 1):
    print(people[i+1])

for i in range(0, 3):
    print(f'Iterator: {i}')

# While loops
count = 0
while count <= 5:
    print(f'Count: {count}')
    count += 1