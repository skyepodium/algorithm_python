while True:
    # 1. input
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    # 2. init
    a, b = str(a)[::-1], str(b)[::-1]
    r = max(len(a), len(b))
    res = 0

    # 3. check carry
    carry = 0
    for i in range(r):
        a_num = int(a[i]) if i < len(a) else 0
        b_num = int(b[i]) if i < len(b) else 0
        s = a_num + b_num + carry
        if s >= 10:
            res += 1
            carry = 1
        else:
            carry = 0

    print(res)

