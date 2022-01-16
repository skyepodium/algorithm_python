from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.n = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        value = self.d.pop(key)
        self.d[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.pop(key)
        else:
            if self.n > 0:
                self.n -= 1
            else:
                self.d.popitem(last=False)
        self.d[key] = value

lr = LRUCache(2)
print(None)
print(lr.get(2))
print(lr.put(2, 6))
print(lr.get(1))
print(lr.put(1, 5))
print(lr.put(1, 2))
print(lr.get(1))
print(lr.get(2))
