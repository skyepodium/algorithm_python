class Node:
    def __init__(self, val, min_val):
        self.val = val
        self.next = None
        self.min_val = min_val


class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        node = Node(val, min(val, self.head.min_val) if self.head else val)
        node.next = self.head
        self.head = node

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min_val
