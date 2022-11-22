n, x = map(int, input().split())

nums = list(map(int, input().split()))
res = 0
l = 0
sum_val = 0
sum_val_count = 0
for r, num in enumerate(nums):
    sum_val += num
    if r - l + 1 >= x:
        if sum_val > res:
            res = sum_val
            sum_val_count = 1
        elif sum_val != 0 and sum_val == res:
            sum_val_count += 1
        sum_val -= nums[l]
        l += 1

if res == 0:
    print("SAD")
else:
    print(res)
    print(sum_val_count)
