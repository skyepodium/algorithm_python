from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # 1. get_binary
        def get_one_cnt(num):
            one_cnt = 0
            while num > 0:
                if num % 2 == 1: one_cnt += 1
                num //= 2
            return one_cnt

        # 2. init
        arr_list = [(x, get_one_cnt(x)) for x in arr]

        # 3. sort
        arr_list.sort(key=lambda x: (x[1], x[0]))

        return [x[0] for x in arr_list]

sl = Solution()
arr = [0,1,2,3,4,5,6,7,8]
res = sl.sortByBits(arr)
print('res', res)