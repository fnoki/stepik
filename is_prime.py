def is_prime(num):
    balance = 0
    num = int(num)
    for i in range(1, num):
        if num % i == 0:
            balance += 1

    if balance < 2 and num != 1:
        return True
    else:
        return False

print(is_prime(72))