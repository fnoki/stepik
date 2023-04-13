stroke: str = input()
rubles = 0
pennies = 0

while stroke != "":
    stroke = stroke.replace(stroke[0], "",1)
    pennies += 60

while pennies >= 100:
    rubles += 1
    pennies -= 100

print(f'{rubles} р. {pennies} коп.')