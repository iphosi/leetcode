def isHappy(n: int) -> bool:
    num = str(n)

    history = {num}

    while True:
        num = str(sum(int(char) ** 2 for char in num))
        if num == '1':
            return True
        elif num in history:
            return False
        else:
            history.add(num)
