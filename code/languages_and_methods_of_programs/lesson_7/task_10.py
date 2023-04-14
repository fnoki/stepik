numbers = [0, -5, 12, 5, -31, 36, 9, -12, 4, 3]

list_positive_numbers = list(filter(lambda x: True if x % 2 != 0 and x > 0 else False, numbers))
print(list_positive_numbers)