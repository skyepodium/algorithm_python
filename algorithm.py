class Solution:
    def romanToInt(self, s: str) -> int:
        # roman to integer
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # result
        result = 0
        # loop through the string
        for i in range(len(s)):
            # if the current string is less than the next string, then it is a subtraction
            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                result -= roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]
        return result
