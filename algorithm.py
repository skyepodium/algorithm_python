a = [1, 2, 3]
b = [1, 2]

print(zip(a, b))

for x, y, in zip(a, b):
    print(x, y)