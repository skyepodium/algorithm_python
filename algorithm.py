def solution(arrayA, arrayB):
    # 1. init
    a_gcd, b_gcd = arrayA[0], arrayB[0]

    # 2. gcd
    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    # 3. loop
    for a, b in zip(arrayA, arrayB):
        a_gcd, b_gcd = gcd(a_gcd, a), gcd(b_gcd, b)

    # 4. check
    for a, b in zip(arrayA, arrayB):
        if a_gcd != 0 and b % a_gcd == 0:
            a_gcd = 0

        if b_gcd != 0 and a % b_gcd == 0:
            b_gcd = 0

    # 5. return
    return max(a_gcd, b_gcd)

arrayA = [10, 17]
arrayB = [5, 20]

arrayA = [10, 20]
arrayB = [5, 17]

arrayA = [14, 35, 119]
arrayB = [38, 30, 102]

print(solution(arrayA, arrayB))