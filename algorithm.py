class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1. init
        stack = []
        res = [0 for _ in range(len(temperatures))]

        # 2. loop
        for i in range(len(temperatures)):
            cur = temperatures[i]

            while stack and temperatures[stack[-1]] < cur:
                top = stack.pop()
                res[top] = i - top

            stack.append(i)

        return res