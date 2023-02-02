class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        result = []

        size = len(candidates)

        def go(idx, sumVal, stack):
            if sumVal >= target:
                if sumVal == target:
                    result.append(stack[:])
                return

            for i in range(idx, size):
                stack.append(candidates[i])
                go(i, sumVal + candidates[i], stack)
                stack.pop()

        go(0, 0, [])

        return result