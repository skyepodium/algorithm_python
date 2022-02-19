class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n // 2 + 1):
            if "0" in str(i) or "0" in str(n - i): continue

            if i + n - i == n:
                return [i, n - i]