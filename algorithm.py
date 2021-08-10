class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        result = []

        def go(idx, stack, remain):
            if remain == 0:
                result.append(stack[:])
                return

            for i in range(idx + 1, n + 1):
                stack.append(i)
                go(i, stack, remain - 1)
                stack.pop()

        go(0, [], k)

        return result


sl = Solution()

n = 4
k = 2

# n = 1
# k = 1

res = sl.combine(n, k)

print(res)