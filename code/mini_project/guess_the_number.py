from random import randint


def start():
    print("Привет! Твое загаданное число в диапазоне 1, 100")
    hidden_number = randint(1, 100)
    program(hidden_number)


def program(ran: int):
    person_int = -1
    count_try = 1
    while person_int != ran:
        person_int = int(input(f"Попробуй угадать загаданное число с {count_try} попытки: "))

        if is_valid(person_int):
            if person_int > ran:
                print("Твое число больше загаданного)\n")
                count_try += 1
            elif person_int < ran:
                print("Твое число меньше загаданного О.о\n")
                count_try += 1
            else:
                print("Поздравляю! Ты угадал!")
                end()
                break
        else:
            print('Ха-ха, попробуй ввести правильно число от 1 до 100 :)\n')
            person_int = -1


def is_valid(person_value: any):
    if type(person_value) == int and (0 <= person_value < 101):
        return True
    else:
        return False


def end():
    again = "Ты выиграл в прошлой!"
    print(again)
    while again != 'y' or again != 'n':
        again = input("Сыграем еще? (y/n) ")
        if again == "y":
            start()
        elif again == "n":
            print("Хорошего дня!)\n")
            input()
        else:
            print('Ты ввел неправильное значение\n')


start()
