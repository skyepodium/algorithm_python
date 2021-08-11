def solution(scores):
    answer = ""

    def get_grade(val):
        res = "F"
        if val >= 90: res = "A"
        elif val >= 80: res = "B"
        elif val >= 70: res = "C"
        elif val >= 50: res = "D"
        print(res)
        return res

    size = len(scores)
    for j in range(size):
        cur_list = []
        cur_val = scores[j][j]
        for i in range(size):
            cur_list.append(scores[i][j])

        cur_list.sort()

        if cur_list[0] == cur_val and cur_list[0] != cur_list[1]:
            answer += get_grade(sum(cur_list[1:]) / len(cur_list[1:]))
            continue
        if cur_list[size-1] == cur_val and cur_list[size-1] != cur_list[size-2]:
            answer += get_grade(sum(cur_list[:size-1]) / len(cur_list[:size-1]))
            continue
        answer += get_grade(sum(cur_list) / len(cur_list))

    return answer



s = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
s = [[70,49,90],[68,50,38],[73,31,100]]
res = solution(s)

print(res)