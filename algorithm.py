
def solution(price, money, count):
    result = (count * (count + 1)) // 2 * price - money

    return result if result > 0 else 0


p = 3
m = 20000
c = 4

res = solution(p, m, c)

print(res)

