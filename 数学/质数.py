def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True


def is_prime(x):
    if x == 2:
        return True
    elif x % 2 == 0:
        return False

    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True
