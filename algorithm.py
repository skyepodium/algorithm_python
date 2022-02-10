class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i, a in enumerate(arr):
            for j, b in enumerate(arr):
                if i == j: continue

                if a * 2 == b:
                    return True
        return False