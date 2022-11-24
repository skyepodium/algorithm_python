while True:
    n = int(input())
    if n == 0:
        break

    while True:
        n = sum([int(x) for x in list(str(n))])
        if n < 10:
            print(n)
            break