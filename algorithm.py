def solution(s):
    # 1. init
    n = len(s)
    res = n

    # 2. loop
    for i in range(1, n//2 + 1):
        t = ""
        prev = ""
        cnt = 1
        is_append = False
        for j in range(0, n, i):
            cur = s[j:j+i]
            if cur == prev:
                cnt += 1
                is_append = False
            else:
                t += f"{cnt}{prev}" if cnt >= 2 else prev
                prev = cur
                cnt = 1
                is_append = True
        if not is_append:
            t += f"{cnt}{prev}" if cnt >= 2 else prev
        else:
            t += cur

        res = min(res, len(t))

    return res


s = "aabbaccc"
s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"

res = solution(s)

print('res', res)
