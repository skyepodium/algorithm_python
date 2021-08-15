def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    res = 0
    for i in range(len(A)):
        res += A[i] * B[i]

    return res