class Solution:
    def countEven(self, num: int) -> int:
        # 1. init
        res = 0

        # 2. loop
        for i in range(1, num+1):
            str_num = str(i)
            nums = [int(j) for j in str_num]
            sum_nums = sum(nums)

            if sum_nums % 2 == 0:
                res += 1

        return res

sl = Solution()
num = 30
res = sl.countEven(num)

print('res', res)