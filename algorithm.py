t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    s = sorted(nums)
    first_max, second_max = s[-1], s[-2]

    res = []
    for num in nums:
        if num != first_max:
            res.append(num - first_max)
        else:
            res.append(num - second_max)
    print(*res)