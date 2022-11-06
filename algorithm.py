a, b = map(int, input().split())

str_a, str_b = str(a), str(b)

min_val = int(str_a.replace('6', '5')) + int(str_b.replace('6', '5'))
max_val = int(str_a.replace('5', '6')) + int(str_b.replace('5', '6'))

print(f"{min_val} {max_val}")