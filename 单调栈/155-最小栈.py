class MinStack:
    def __init__(self):
        self.stack = []
        self.mono_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mono_stack or self.mono_stack[-1] >= val:
            self.mono_stack.append(val)

    def pop(self) -> None:
        if self.mono_stack[-1] == self.stack.pop():
            self.mono_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mono_stack[-1]
