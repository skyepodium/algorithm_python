l = list(map(int, input().split()))

# 1. init
res = int(1e6)

# 2. sort
l.sort()

# 3. gcd
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        for k in range(j + 1, len(l)):
            a, b, c = l[i], l[j], l[k]

            t = (b*c) / gcd(b, c)
            r = (a*t) / gcd(a, t)

            res = min(res, int(r))

print(res)


