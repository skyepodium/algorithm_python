def solution(s):
    stack = []

    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False

            if stack[len(stack) - 1] == "(":
                stack.pop()
            else:
                return False

    if len(stack) > 0:
        return False

    return True