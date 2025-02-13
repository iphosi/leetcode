def monotoneIncreasingDigits(n: int) -> int:
    digits = list(str(n))
    num_digits = len(digits)

    if len(set(digits)) == 1:
        return n

    i = 0

    while i < num_digits - 1 and int(digits[i]) <= int(digits[i + 1]):
        i += 1

    while i > 0 and int(digits[i]) == int(digits[i - 1]):
        i -= 1

    if i == num_digits - 1:
        return n

    digits[i] = str(int(digits[i]) - 1)

    digits[i + 1:] = ["9"] * (num_digits - i - 1)

    j = 0

    while j < num_digits and digits[j] == "0":
        j += 1

    return int("".join(digits[j:]))
