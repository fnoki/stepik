numbers = input()
len_numbers = len(numbers)
exit = ''
if len_numbers > 3:
    list_numbers = list(numbers[::-1])
    count_iteration = 0
    for i in range(3, len(list_numbers), 3):
        list_numbers.insert(i + count_iteration, ",")
        count_iteration += 1
    list_numbers = list_numbers[::-1]

    for i in list_numbers:
        exit += str(i)
    print(exit)
else:
    print(numbers)
