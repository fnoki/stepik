from functools import reduce
numbers = [0, -5, 12, 5, -31, 36, 9, -12, 4, 3]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)
