class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    def get_idx(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self.get_idx(key)

        node = self.table[idx]
        # 1) not exist
        if not node: self.table[idx] = ListNode(key, value)

        # 2) exist
        else:
            prev = None

            while node:
                # duplicated key
                if node.key == key:
                    node.value = value
                    break
                # search
                prev, node = node, node.next
            # not found
            if not node: prev.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = self.get_idx(key)

        node = self.table[idx]
        res = -1

        while node:
            if node.key == key:
                res = node.value
                break

            node = node.next

        return res

    def remove(self, key: int) -> None:
        idx = self.get_idx(key)

        prev, node = None, self.table[idx]

        while node:
            if node.key == key:
                if not prev:
                    self.table[idx] = node.next
                    return
                elif not node.next:
                    prev.next = None
                    return
                else:
                    prev.next = node.next
                    return

            prev, node = node, node.next

        return None


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"key: {self.key} value: {self.value} next: {self.next}"

m = MyHashMap()

m.put(1, 1)
print(m.get(1))
m.remove(1)
print(m.get(1))

m.put(1, 1)
m.put(1001, 2)
m.put(1000001, 3)
print(m.get(1))
print(m.get(1001))
print(m.get(1000001))
print()
m.remove(1001)
print(m.get(1))
print(m.get(1001))
print(m.get(1000001))
print()
m.remove(1)
print(m.get(1))
print(m.get(1001))
print(m.get(1000001))
