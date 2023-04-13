Timur = input()
Ruslan = input()

if (Timur == "камень" and Ruslan == "бумага") or (Timur == 'ножницы' and Ruslan == "камень") or (Timur == "бумага" and Ruslan == "ножницы"):
    print("Руслан")
elif Timur == Ruslan:
    print("ничья")
else:
    print("Тимур")