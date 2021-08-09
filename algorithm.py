class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        result = []
        size = len(nums)

        def go(idx, stack):
            if idx >= size:
                result.append(list(stack))
                return

            for num in nums:
                if num not in stack:
                    stack.append(num)
                    go(idx + 1, stack)
                    stack.pop()

        go(0, [])

        return result


sl = Solution()
nums = [1,2,3]
res = sl.permute(nums)

print(res)