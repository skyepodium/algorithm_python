a, b = map(int, input().split())
res = "'"
if a == 0:
    res = "Silver"
elif b == 0:
    res = "Gold"
else:
    res = "Alloy"
print(res)
