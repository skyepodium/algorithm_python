from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = 0
        c = Counter(arr)
        for key, val in c.items():
            if val == 1: cnt += 1
            if cnt >= k:
                return key
        return ""