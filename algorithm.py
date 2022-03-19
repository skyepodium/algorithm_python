from collections import defaultdict


class Node:
    def __init__(self):
        self.is_end = False
        self.child = defaultdict(Node)


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        c = self.root
        for w in word:
            c = c.child[w]
        c.is_end = True

    def search(self, word: str) -> bool:
        c = self.root
        for w in word:
            c = c.child.get(w)
            if not c: return False
        return c.is_end

    def startsWith(self, prefix: str) -> bool:
        c = self.root
        for w in prefix:
            c = c.child.get(w)
            if not c: return False
        return True
