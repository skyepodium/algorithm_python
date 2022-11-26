n = int(input())

d = {}

for i in range(1, n + 1):
    num = i
    sum_val = num
    while num > 0:
        sum_val += num % 10
        num //= 10
    if sum_val not in d:
        d[sum_val] = i
        if sum_val == n:
            break

print(d[n] if n in d else 0)