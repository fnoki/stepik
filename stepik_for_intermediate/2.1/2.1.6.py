number = input()

if len(number) == 5:
    print(int(number[::-1]))
elif len(number) == 6:
    print(int(number[0] + number[1:][::-1]))
