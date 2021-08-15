def solution(left, right):
    answer = 0

    def get_cnt(num):
        res = 0
        for i in range(1, num + 1):
            if num % i == 0:
                res += 1
        return res & 1 != 1

    for i in range(left, right + 1):
        if get_cnt(i):
            answer += i
        else:
            answer -= i

    return answer