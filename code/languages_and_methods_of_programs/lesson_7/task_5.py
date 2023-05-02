import json
json_file = open("employee.json", "r")

json_str = json.load(json_file) # записать список из файла в переменную
print(type(json_str))
