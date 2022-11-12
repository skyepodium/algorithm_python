def solution(n,a,b):
    # 1. init
    res = 0
    a -= 1
    b -= 1

    # 2. swap
    if a > b:
        a, b = b, a

    def next_round(num):
        if num % 2 == 1:
            num -= 1

        return num // 2

    # 3. loop
    while a >= 0 and b >= 0:
        res += 1
        if a % 2 == 0 and a + 1 == b:
            break

        a = next_round(a)
        b = next_round(b)

    return res

n = 8
a = 4
b = 7

res = solution(n, a, b)
print('res', res)
