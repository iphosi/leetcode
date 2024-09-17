def countAndSay(n: int) -> str:
    def get_rle(digits):
        if len(digits) == 1:
            return "1" + digits

        rle = ""
        count = 1
        i = 1

        while i < len(digits):
            if digits[i] == digits[i - 1]:
                count += 1
            else:
                rle += (str(count) + digits[i - 1])
                count = 1
            i += 1

        rle += (str(count) + digits[i - 1])

        return rle

    result = "1"

    if n == 1:
        return result
    else:
        for _ in range(1, n):
            result = get_rle(result)

        return result
