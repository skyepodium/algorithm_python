def solution(array, commands):
    answer = []

    for s, e, n in commands:
        answer.append(sorted(array[s - 1:e])[n - 1])

    return answer