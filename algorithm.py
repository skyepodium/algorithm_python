from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # 1. init
        res = []
        m = len(potions)

        # 2. sort
        potions.sort()

        # 3. lower bound
        def lower_bound(spell):
            s, e = 0, m

            while s < e:
                mid = s + (e - s) // 2
                if spell * potions[mid] < success:
                    s = mid + 1
                else:
                    e = mid

            return e

        # 4. loop
        for spell in spells:
            index = lower_bound(spell)
            success_cnt = m - index
            res.append(success_cnt)

        return res

sl = Solution()

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

res = sl.successfulPairs(spells, potions, success)

print('res', res)