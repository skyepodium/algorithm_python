def solution(answers):
    cnt = [0, 0, 0]
    size = len(answers)
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    one = (size // len(one) + 1) * one
    two = (size // len(two) + 1) * two
    three = (size // len(three) + 1) * three

    for i in range(len(answers)):
        val = answers[i]

        if val == one[i]:
            cnt[0] += 1
        if val == two[i]:
            cnt[1] += 1
        if val == three[i]:
            cnt[2] += 1

    max_val = max(cnt)

    res = []
    for i in range(len(cnt)):
        if cnt[i] == max_val:
            res.append(i + 1)

    return res