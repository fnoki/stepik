# на самом деле это задача от 1 до 2, просто они практически одинаковы и легче их записать так...

file_name = input("Введите название для текстового документа: ")

with open(file_name, 'w') as file:
    for i in range(int(input("Введите количество итераций: "))):
        file.write(input(f"Введите {i} строку: ") + "\n")