from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []

    for token in tokens:
        if token not in {'+', '-', '*', '/'}:
            stack.append(int(token))
        else:
            num_1 = stack.pop()
            num_2 = stack.pop()

            if token == '+':
                stack.append(num_2 + num_1)
            elif token == '-':
                stack.append(num_2 - num_1)
            elif token == '*':
                stack.append(num_2 * num_1)
            elif token == '/':
                stack.append(int(num_2 / num_1))

    return stack[0]
