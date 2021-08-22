class MyQueue:

    def __init__(self):
        self.left = []
        self.right = []

    def push(self, x: int) -> None:
        self.right.append(x)

    def pop(self) -> int:
        self.peek()
        return self.left.pop()

    def peek(self) -> int:
        if not self.left:
            while self.right:
                self.left.append(self.right.pop())
        return self.left[-1]

    def empty(self) -> bool:
        return len(self.left) == 0 and len(self.right) == 0