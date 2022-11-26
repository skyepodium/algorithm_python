n = int(input())

i = 666
cnt = 0
while True:
    if "666" in str(i):
        cnt += 1
    if cnt >= n:
        break
    i += 1

print(i)