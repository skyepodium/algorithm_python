class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        arr.sort(key=lambda x: -x)
        for i, a in enumerate(arr):
            if a not in d:
                d[a] = i

            b = a * 2
            if b in d and d[b] != i:
                return True

            c = a / 2
            if c in d and d[c] != i:
                return True
        return False
