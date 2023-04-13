mass = input().split(" ")
count_iteration = 0
exit_num = 0
for i in mass[1:]:
    if int(i) > int(mass[count_iteration]):
        exit_num += 1
    count_iteration += 1
print(exit_num)