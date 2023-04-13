_list = input().split()
min_int = _list[0]
counter = 1
for i in _list:
    if int(i) > int(min_int):
        min_int = i
        counter += 1
print(counter)