class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        digits[idx] += 1

        while idx >= 0:
            val = digits[idx]

            if val >= 10:
                digits[idx] = 0
                if idx == 0:
                    digits = [1] + digits
                else:
                    digits[idx - 1] += 1

            idx -= 1

        return digits;   