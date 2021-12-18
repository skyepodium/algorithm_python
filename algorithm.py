class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0

        while num > 0:
            result += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1

        return result