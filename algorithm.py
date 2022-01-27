class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # 1. init
        n = len(arr)
        res = 0

        # 2. loop
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    q, w, e = arr[i], arr[j], arr[k]
                    if abs(q - w) <= a and abs(w - e) <= b and abs(q - e) <= c:
                        res += 1
    
        return res