from pyscript import Element
current_value = ""
first_value = 0
remember_operation = ''
paragraph = Element("current-value")


def calc(value: int):
    global current_value
    global paragraph

    if value >= 0:
        if current_value == "0":
            current_value = ''  
        current_value += str(value)
    elif value == -1:
        if len(current_value) == 1:
            current_value = "0"
        else:
            current_value = current_value[:-1]
    elif value == -2:
        current_value += str('.')
    elif value == -3:
        current_value = "0"

    paragraph.write(current_value)


def arithmetic_operation(value: str):
    global current_value
    global first_value
    global remember_operation
    global paragraph
    remember_operation = value

    if int(current_value) != 0:
        first_value = int(current_value)
        current_value = "0"
    if remember_operation == "coren":
        current_value = str(int(first_value ** 0.5))
    elif remember_operation == "corenx2":
        current_value = str(int(first_value) ** 2)
    elif remember_operation == "corenx3":
        current_value = str(int(first_value) ** 3)
    paragraph.write(current_value)


def equals():
    global current_value
    global first_value
    global remember_operation
    global paragraph

    if remember_operation == "+":
        current_value = str(first_value + int(current_value))
    elif remember_operation == "-":
        current_value = str(first_value - int(current_value))
    elif remember_operation == "/":
        current_value = str(first_value / int(current_value))
    elif remember_operation == "*":
        current_value = str(first_value * int(current_value))
    elif remember_operation == "**":
        current_value = str(first_value ** int(current_value))

    paragraph.write(current_value)
    