class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        stack, counter, seen = [], Counter(s), set()

        for c in s:
            counter[c] -= 1

            if c in seen:
                continue

            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)