def solution(sizes):
    # 1. init
    x_max, y_max = 0, 0

    # 2. loop
    for x, y in sizes:
        if x > y:
            x, y = y, x
        x_max, y_max = max(x, x_max), max(y, y_max)

    return x_max * y_max