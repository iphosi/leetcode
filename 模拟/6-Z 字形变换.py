def convert(s: str, numRows: int) -> str:
    if numRows < 2:
        return s

    result = ["" for _ in range(numRows)]

    curr_row = 0
    direction = -1

    for char in s:
        result[curr_row] += char
        if curr_row == 0 or curr_row == numRows - 1:
            direction *= -1
        curr_row += direction

    return "".join(result)
