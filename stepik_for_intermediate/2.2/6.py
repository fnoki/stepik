count_iteration = int(input())
_list = []
for i in range(0, count_iteration):
    _list.append(int(input()))
num_who_guess = int(input())

copy_list = _list
checker = False
iteration = 0
for i in _list:
    copy_iteration = 0
    for w in copy_list:
        if i * w == num_who_guess and iteration != copy_iteration:
            checker = True
        copy_iteration += 1
    iteration += 1

if checker:
    print("ДА")
else:
    print("НЕТ")