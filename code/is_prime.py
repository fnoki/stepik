_input = int(input())


def is_prime(num: int) -> bool:
    balance = 0
    for i in range(1, num):
        if num % i == 0:
            balance += 1

    if balance < 2 and num != 1:
        return True
    else:
        return False

print(is_prime(_input))
