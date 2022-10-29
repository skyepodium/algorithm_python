def solution(common):
    return common[-1] + common[2] - common[1] if common[1] - common[0] == common[2] - common[1] else common[-1] * int(common[2] / common[1])


common = [1, 2, 3, 4]
common = [2, 4, 8]
print(solution(common))