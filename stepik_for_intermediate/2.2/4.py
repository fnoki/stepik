_list = input().split()
exit = [_list[-1]]
_list.pop(-1)

for i in range(0, len(_list)):
    exit.append(_list[-len(_list) + i])
print(' '.join(exit))