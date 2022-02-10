class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for i, a in enumerate(arr):
            d[a] = i

        for j, b in enumerate(arr):
            c = b * 2
            if c in d and d[c] != j:
                return True
        return False