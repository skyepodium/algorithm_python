def solution(n, t, m, p):

    def int_to_base_str(num, base):
        res = ""
        while num > 0:
            remain = num % base
            if remain >= 10:
                res += chr(ord('A') + remain % 10)
            else:
                res += str(remain)
            num //= base

        if res == "":
            res = "0"

        return res[::-1]

    r = ""
    for i in range(t * m):
        r += int_to_base_str(i, n)

    res = ""
    for i in range(p, t*m+1, m):
        idx = i - 1
        res += r[idx]

    return res


n, t, m, p = 2, 4, 2, 1
n, t, m, p = 16, 16, 2, 1
n, t, m, p = 16, 16, 2, 2

res = solution(n, t, m, p)

print('res', res)

print(len("13579BDF01234567"))

