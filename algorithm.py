class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # 1. init
        diff = len(arr) // 4

        # 2. loop
        for i in range(len(arr) - diff):
            if arr[i] == arr[i + diff]:
                return arr[i]

        return arr[-1]
