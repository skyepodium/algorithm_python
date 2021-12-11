'''
시간 복잡도: O(n)
공간 복잡도: O(n)
사용한 알고리즘: 반복문
사용한 자료구조: 트리
'''

def solution(enroll, referral, seller, amount):
    # 1. init
    n = len(enroll)
    answer = [0 for _ in range(n)]
    p = {}
    idx_dict = {}
    idx = 0

    # 2. make tree
    for e, r in zip(enroll, referral):
        p[e] = r
        idx_dict[e] = idx
        idx += 1

    # 3. loop
    for s, a in zip(seller, amount):
        a *= 100
        remain = a
        cur = s

        while remain > 0 and cur != '-':
            # 1) check
            cur_idx = idx_dict[cur]

            # 2) calculate
            upper = int(remain * 0.1)
            mine = remain - upper
            if upper < 1:
                mine = remain
                upper = 0

            # 3) update
            answer[cur_idx] += mine
            cur = p[cur]
            remain = upper

    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

# enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
# referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
# seller = ["sam", "emily", "jaimie", "edward"]
# amount = [2, 3, 5, 4]

res = solution(enroll, referral, seller, amount)

print('res', res)

