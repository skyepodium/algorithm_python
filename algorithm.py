class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # 1. init
        n = len(arr)
        res = 0

        # 2. loop
        for i in range(1, n + 1, 2):
            for j in range(n - i + 1):
                res += sum(arr[j:j + i])

        return res