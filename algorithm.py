import re

def solution(n, k):
    # 1. init
    res = 0

    # 2. int_to_base
    def int_to_base(n, k):
        r = ""
        while n > 0:
            r += str(n % k)
            n //= k
        return r[::-1]

    # 3. int_to_base
    def is_prime(val):
        if val < 2: return False

        for i in range(2, int(val ** 0.5) + 1):
            if val % i == 0: return False
        return True

    num = int_to_base(n, k)

    # 4. check
    ### 1) not zero
    if num.count("0") == 0 and is_prime(int(num)):
        res += 1

    ### 2) left
    for c in re.findall("^([1-9]+)0", num):
        if is_prime(int(c)):
            res += 1

    ### 3) left
    for c in re.findall("0([1-9]+)$", num):
        if is_prime(int(c)):
            res += 1

    ## 4) both
    for x in re.findall("(?=0([1-9]+)0)", num):
        if is_prime(int(x)):
            res += 1

    return res


n = 437674
k = 3

n = 110011
k = 10

res = solution(n, k)

print('res', res)
