from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # 1. init
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        half_size = (sum_alice + sum_bob) // 2
        s = set(aliceSizes)

        # 2. loop
        for b in bobSizes:
            remain = half_size - (sum_bob - b)
            if remain in s:
                return [remain, b]

        return [-1, -1]


sl = Solution()
aliceSizes = [1,1]
bobSizes = [2,2]

aliceSizes = [1,2]
bobSizes = [2,3]

aliceSizes = [2]
bobSizes = [1,3]

aliceSizes = [2, 2]
bobSizes = [1, 1]
res = sl.fairCandySwap(aliceSizes, bobSizes)

print('res', res)