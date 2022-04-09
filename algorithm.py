import collections


def solution(participant, completion):
    return list((collections.Counter(participant) - collections.Counter(completion)).keys())[0]


p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]

res = solution(p, c)

print('res', res)