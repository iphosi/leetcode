

class MyStack:
    def __init__(self):
        self.data_queue = []
        self.temp_queue = []

    def push(self, x: int) -> None:
        self.data_queue.append(x)

    def pop(self) -> int:
        while len(self.data_queue) > 1:
            self.temp_queue.append(self.data_queue.pop(0))
        while self.temp_queue:
            self.data_queue.append(self.temp_queue.pop(0))

        return self.data_queue.pop(0)

    def top(self) -> int:
        top = self.pop()
        self.push(top)

        return top

    def empty(self) -> bool:
        return len(self.data_queue) == 0
