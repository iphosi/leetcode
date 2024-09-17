

def isValid(s: str) -> bool:
    stack = []

    for char in s:
        if char in {'(', '{', '['}:
            stack.append(char)
        elif stack and stack[-1] + char in {'()', '{}', '[]'}:
            stack.pop()
        else:
            return False

    return True if not stack else False
