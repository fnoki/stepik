import json
json_file = open("employee.json", "r")

json_str = json.load(json_file)
print(type(json_str))
