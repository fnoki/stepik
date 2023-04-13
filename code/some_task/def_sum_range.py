start, end = int(input("начало: ")), int(input("конец: "))


def sum_range(_start: int, _end: int) -> str:
    return f"Сумма в диапазоне равняется: {sum(range(_start, _end + 1))}"


print(sum_range(start, end))
