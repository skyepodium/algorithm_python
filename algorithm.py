class Solution:
    def countLargestGroup(self, n: int) -> int:
        # 1. init
        d = {}
        max_val = 0
        result = 0

        # 2. loop
        for i in range(1, n + 1):
            num_str = str(i)

            sum_val = 0
            for c in num_str:
                sum_val += int(c)

            if sum_val not in d:
                d[sum_val] = 1
            else:
                d[sum_val] += 1

            max_val = max(max_val, d[sum_val])

        # 3. result
        for key in d:
            if d[key] == max_val:
                result += 1

        return result


sl = Solution()
n = 13
n = 2
print(sl.countLargestGroup(n))
