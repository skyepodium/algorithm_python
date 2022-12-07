def main():
    # 1. input
    n = int(input())
    life = list(map(int, input().split()))
    joy = list(map(int, input().split()))

    # 2. init
    MAX_LIFE = 100
    d = [[0 for _ in range(MAX_LIFE + 1)] for _ in range(n + 1)]

    # 3. loop
    for i in range(n):
        for j in range(MAX_LIFE + 1):
            if j - life[i] > 0:
                d[i][j] = max(d[i-1][j], d[i-1][j - life[i]] + joy[i])
            else:
                d[i][j] = max(d[i-1][j], d[i][j])

    return d[n-1][MAX_LIFE]


if __name__ == '__main__':
    print(main())