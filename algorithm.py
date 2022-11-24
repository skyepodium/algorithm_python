n = int(input())

a = bin(n)[2:].zfill(32)
b = a.replace('1', '2').replace('0', '1').replace('2', '0')

m = int(b, 2)
m += 1

b = bin(m)[2:]
b = b[:32]

res = 0

for q, w in zip(a, b):
    if q != w:
        res += 1

print(res)