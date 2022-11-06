a = [0 for _ in range(21)]

a[0], a[1] = 0, 1

for i in range(2, 21):
    a[i] = a[i-1] + a[i-2]

n = int(input())
print(a[n])
