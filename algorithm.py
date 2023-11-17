class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = ""
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) == 1:
                    result += s[stack.pop() + 1:i]
                else:
                    stack.pop()
        return result
