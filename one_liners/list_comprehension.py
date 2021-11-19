# Create employees dictionary of salaries
employees = {'Alice' : 100000,
             'Bob' : 99817,
             'Carol' : 122908,
             'Frank' : 88123,
             'Eve' : 93121}

top_earners = []

for k, v in employees.items():
    if v >= 100000:
        top_earners.append((k, v))

print(top_earners)

print([x**2 for x in range(10)])

top_earners2 = [(k, v) for k, v in employees.items() if v >= 100000]

print(top_earners2)
