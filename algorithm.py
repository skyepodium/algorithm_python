"""
시간 복잡도: O(1)
공간 복잡도: O(1)
사용한 알고리즘: 가우스 공식
사용한 자료구조: ..
"""
def solution(price, money, count):
    result = (count * (count + 1)) // 2 * price - money

    return result if result > 0 else 0


p = 3
m = 20000
c = 4

res = solution(p, m, c)

print(res)

