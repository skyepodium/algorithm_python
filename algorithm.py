def solution(arr):
    s = []

    for a in arr:
        if len(s) == 0 or s[-1] != a:
            s.append(a)

    return s