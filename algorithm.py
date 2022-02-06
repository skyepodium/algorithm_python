class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size
        self.load_factor = 0.6
        self.count = 0

    def resize(self):
        # 기존 요소 모두 탐색
        prev_element = self.all_element()
        # 테이블 크기 * 2
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        for key, value in prev_element:
            self.put(key, value)

    def all_element(self):
        res = []
        for node in self.table:
            while node:
                res.append((node.key, node.value))
                node = node.next
        return res

    def hash_code(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        h = self.hash_code(key)

        node = self.table[h]
        # 1) 노드가 비어있는 경우
        if not node:
            self.count += 1
            self.table[h] = ListNode(key, value)
        # 2) 노드에 값이 들어있는 경우
        else:
            prev = None
            while node:
                # 노드를 찾은 경우 - value 업데이트
                if node.key == key:
                    node.value = value
                    break
                # 다음 노드로 진행
                prev, node = node, node.next
            # 노드를 찾지 못한 경우 - 맨 뒤에 새로우 노드 추가
            if not node:
                self.count += 1
                prev.next = ListNode(key, value)

        if self.count / self.size >= self.load_factor:
            self.resize()

    def get(self, key: int) -> int:
        h = self.hash_code(key)

        node = self.table[h]
        res = -1

        while node:
            # 노드를 찾은 경우 - value 반환
            if node.key == key:
                res = node.value
                break
            # 다음 노드 탐색
            node = node.next
        return res

    def remove(self, key: int) -> None:
        h = self.hash_code(key)

        prev, node = None, self.table[h]

        while node:
            if node.key == key:
                self.count -= 1
                # 1) 제일 첫번재 노드 삭제
                if not prev:
                    self.table[h] = node.next
                    break
                # 2) 제일 마지막 노드 삭제
                elif not node.next:
                    prev.next = None
                    break
                # 3) 가운데 노드 삭제
                else:
                    prev.next = node.next
                    break
            # 다음 노드 탐색
            prev, node = node, node.next
        return


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
