from datetime import datetime
from pyscript import Element
current_value = ""
first_value = 0
remember_operation = ''

paragraph = Element("current-value")


def calc(value: int):
    global current_value
    global paragraph

    current_value += str(value)
    paragraph.write(current_value)


def arithmetic_operation(value: str):
    global current_value
    global first_value
    global remember_operation

    remember_operation = value
    if int(current_value) != 0:
        first_value = int(current_value)
        current_value = ""
    if remember_operation == "coren":
        current_value = first_value ** 0.5
        paragraph.write(current_value)


def equals():
    global current_value
    global first_value
    global remember_operation
    global paragraph

    if remember_operation == "+":
        current_value = str(int(current_value) + first_value)
    elif remember_operation == "-":
        current_value = str(int(current_value) - first_value)
    elif remember_operation == "/":
        current_value = str(int(current_value) / first_value)
    elif remember_operation == "*":
        current_value = str(int(current_value) * first_value)
    elif remember_operation == "**":
        current_value = str(first_value ** int(current_value))

    paragraph.write(current_value)
