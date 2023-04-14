_input = input()
copy_for_while = ""
iteration = 0
counter = 0
max_count = 0
while copy_for_while != _input:
    copy_for_while += _input[iteration]
    if _input[iteration] == "Р":
        counter += 1
        if max_count < counter:
            max_count = counter
    else:
        counter = 0
    iteration += 1
print(max_count)
