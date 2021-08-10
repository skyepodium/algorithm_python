class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        result = []
        size = len(nums)

        def go(idx, stack):
            result.append(stack[:])

            for i in range(idx, size):
                stack.append(nums[i])
                go(i + 1, stack)
                stack.pop()

        go(0, [])

        return result

sl = Solution()

nums = [1, 2, 3]

res = sl.subsets(nums)

print(res)