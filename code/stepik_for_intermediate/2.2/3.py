_list = input().split()
exit = ''

for i in range(1, len(_list), 2):
    exit += _list[i] + " " + _list[i - 1] + " "

if len(_list) % 2 != 0:
    exit += _list[-1]

print(exit)