def decodeString(s: str) -> str:
    stack = []

    for char in s:
        if char == "]":
            char_list = []
            while stack[-1] != "[":
                char_list.append(stack.pop())
            stack.pop()

            digit_list = []
            while stack and stack[-1].isdigit():
                digit_list.append(stack.pop())
            count = int("".join(digit_list[::-1])) if digit_list else 1

            stack.extend(char_list[::-1] * count)
        else:
            stack.append(char)

    return "".join(stack)
