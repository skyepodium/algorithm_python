def dfs(idx, num):
    if idx >= 5:
        print('num', num)
        return

    dfs(idx + 1, num + idx)

    dfs(idx + 1, num)


def main():
    dfs(0, 0)


main()
