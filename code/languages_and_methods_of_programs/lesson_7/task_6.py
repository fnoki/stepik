import json
employee = {
    'employee1': {'name': 'Sam', 'age': 35, 'salary': 400000},
    'employee2': {'name': 'Anna', 'age': 29, 'salary': 350000},
    'employee3': {'name': 'John', 'age': 25, 'salary': 250000}
}

json_str = json.dumps(employee)
print(json_str)