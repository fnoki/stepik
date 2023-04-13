Timur = input()
Ruslan = input()
# 'Спок' > 'ножницы', 'камень'

if (Timur == "ножницы") and (Ruslan == "бумага" or Ruslan == 'ящерица'):
    print("Тимур")
elif (Ruslan == "ножницы") and (Timur == "бумага" or Timur == 'ящерица'):
    print("Руслан")
if (Timur == 'бумага') and (Ruslan == "камень" or Ruslan == 'Спок'):
    print("Тимур")
elif (Ruslan == 'бумага') and (Timur == "камень" or Timur == 'Спок'):
    print("Руслан")
if (Timur == 'камень') and (Ruslan == 'ножницы' or Ruslan == "ящерица"):
    print("Тимур")
elif (Ruslan == 'камень') and (Timur == 'ножницы' or Timur == "ящерица"):
    print("Руслан")
if (Timur == "ящерица") and (Ruslan == "Спок" or Ruslan == "бумага"):
    print('Тимур')
elif (Ruslan == "ящерица") and (Timur == "Спок" or Timur == "бумага"):
    print('Руслан')
if (Timur == 'Спок') and (Ruslan == "ножницы" or Ruslan == 'камень'):
    print('Тимур')
elif (Ruslan == 'Спок') and (Timur == "ножницы" or Timur == 'камень'):
    print('Руслан')

if Timur == Ruslan:
    print("ничья")