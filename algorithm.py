class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # 1. init
        n = len(arr)
        cnt = n // 2 + 1 if n % 2 == 1 else n // 2
        res = 0

        # 2. loop
        for i in range(1, n + 1, 2):
            for j in range(n - i + 1):
                res += sum(arr[j:j + i])

        return res