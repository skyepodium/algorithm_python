s = input()
a = [0, 0]

if len(s) == 2:
    a[0], a[1] = int(s[0]), int(s[1])
elif len(s) == 4:
    a[0], a[1] = 10, 10
elif s[1] == '0':
    a[0], a[1] = 10, int(s[2])
else:
    a[0], a[1] = int(s[0]), 10

print(sum(a))