from pyscript import Element
paragraph = Element('name')

more_eight = Element('reg_more_eight')
symbol_upper = Element("first_symbol_upper")

user = {

}

def registration(login:str, password:str):
    global user

    if len(password) >= 8 and not (password in "QWERTYUIOPASDFGHJKLZXCVBNM" or password in "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"):
        user[login] = password
    if len(password) < 8:
        more_eight.write("Пароль меньше 8 символов")
    else:
        more_eight.write("● Пароль должен быть больше 8 символов.")
    if password in "QWERTYUIOPASDFGHJKLZXCVBNM" or password in "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ":
        symbol_upper.write("в пароле нет большого символа")
    else:
        symbol_upper.write(" ● Хотя бы один символ строки должен быть с большой буквы.")

def login(login:str, password:str):
    global user
    global paragraph

    for k,v in user.items():
        if k == login and v == password:
            paragraph.write(login)
