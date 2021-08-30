def solution(number, k):
    # 1. init
    stack = []

    # 2. loop
    for c in number:
        while k > 0 and stack and ord(stack[-1]) < ord(c):
            stack.pop()
            k -= 1

        stack.append(c)

    # 3. exception
    while k > 0:
        stack.pop()
        k -= 1

    return "".join(stack)

res = solution("321", 2)

print('res', res)