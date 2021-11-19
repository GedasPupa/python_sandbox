const employees = {
    'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121
}

const top_earners = []

for  (const [k, v] of Object.entries(employees)) {
    if (v >= 100000) {
        top_earners.push([k, v])
    }
}

console.log(top_earners);

