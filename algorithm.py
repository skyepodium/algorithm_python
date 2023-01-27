class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        result = []
        size = len(nums)
        check = [False for _ in range(21)]

        def go(idx, stack):
            if idx >= size:
                result.append(list(stack))
                return

            for num in nums:
                if not check[num+10]:
                    check[num+10] = True
                    stack.append(num)

                    go(idx + 1, stack)

                    check[num+10] = False
                    stack.pop()

        go(0, [])

        return result