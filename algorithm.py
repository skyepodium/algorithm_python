n = int(input())
a = list(map(int, input().split()))

res = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        res += abs(a[i] - a[j])

print(res * 2)