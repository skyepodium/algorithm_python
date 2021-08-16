def solution(s):
    # 1. shift with slicing
    def shift(s):
        return s[-1] + s[:len(s) - 1]

    # 2. check valid
    def is_valid(s):
        d = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        stack = []
        for c in s:
            if c not in d:
                if not stack:
                    return False

                top = stack.pop()
                if d[top] != c:
                    return False
            else:
                stack.append(c)

        if stack:
            return False

        return True

    # 3. shift and update cnt
    answer = 0
    for i in range(0, len(s)):
        if is_valid(s):
            answer += 1
        s = shift(s)

    return answer