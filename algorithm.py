class MyHashMap:
    def __init__(self):
        self.count = 0
        self.size = 10
        self.deleted_size = 0
        self.table = [None] * self.size
        self.load_factor = 0.6
        self.min_factor = 3

    def _hash_code(self, key):
        return key % self.size

    def __get_entry(self, key):
        hash_key = self._hash_code(key)
        root_idx = hash_key

        for offset in range(self.size):
            new_idx = (root_idx + offset) % self.size
            node = self.table[new_idx]
            if not node or (node.key is not None and node.hash_key == hash_key and node.key == key):
                return new_idx, node

    def resize(self):
        old_table = self.table
        self.size *= self.min_factor
        self.table = [None] * self.size
        self.count = 0
        for node in old_table:
            if node and node.key is not None: self.put(node.key, node.value)

    def put(self, key: int, value: int) -> None:
        new_idx, node = self.__get_entry(key)

        if not node: self.count += 1
        self.table[new_idx] = Node(key, self._hash_code(key), value)

        if (self.deleted_size + self.count) / self.size >= self.load_factor:
            self.resize()

    def get(self, key: int) -> int:
        new_idx, node = self.__get_entry(key)
        if not node: return -1
        else: return node.value

    def remove(self, key: int) -> None:
        new_idx, node = self.__get_entry(key)
        if node and node.key is not None:
            self.table[new_idx] = Node(None, None, None)
            self.count -= 1
            self.deleted_size += 1

class Node:
    def __init__(self, key, hash_key, value):
        self.key = key
        self.hash_key = hash_key
        self.value = value

    def __str__(self):
        return f"key {self.key} hash_key {self.hash_key} value {self.value}"

m = MyHashMap()
m.put(0, 0)
m.put(1, 1)
print("key 0", m.get(0))
print(m.get(1))
m.put(10, 3)
print(m.get(10))
m.remove(1)
print(m.get(10))

a = Node(None, None, None)
b = Node(None, None, None)
print(a == b)