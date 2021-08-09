class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        nums = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]

        result = []
        size = len(digits)

        def go(idx, val):
            if idx >= size:
                if len(val) > 0:
                    result.append("".join(val))
                return

            cur = int(digits[idx])

            for num in nums[cur]:
                val.append(num)
                go(idx + 1, val)
                val.pop()

        go(0, [])

        return result


sl = Solution()

digits = "23"
digits = ""

res = sl.letterCombinations(digits)

print(res)