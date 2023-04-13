start, end = int(input("начало: ")), int(input("конец: "))


def sum_range(start: int, end: int) -> str:
    return f"Сумма в диапазоне равняется: {sum(range(start, end + 1))}"


print(sum_range(start, end))
