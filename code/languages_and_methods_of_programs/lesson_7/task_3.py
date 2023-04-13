file_name = input("Введите название для текстового документа: ")

file = open(file_name, "r")
print("\nfor_file")
for line in file:
    print(line, sep='', end='')
file.close()

file = open(file_name, "r")
print("\nread_file")
print(file.read())
file.close()

file = open(file_name, "r")
print("\nreadline_file")
print(file.readline(3))
file.close()