b = input()

while len(b) % 3 != 0:
    b = "0" + b


res = ""
for i in range(0, len(b), 3):
    cur = b[i:i+3]
    res += str(int(cur, 2))

print(res)