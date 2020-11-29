n, b, h, w = map(int, input().split())

h_list = []
w_list = []
max_val = 10001 * 200
result = max_val

for i in range(h):
    pay = int(input())
    h_list.append(pay)

    w_arr = list(map(int, input().split()))
    w_list.append(w_arr)

for i in range(h):
    if h_list[i] * n > b:
        continue

    check = False
    for room_cnt in w_list[i]:
        if room_cnt >= n:
            check = True

    if not check:
        continue

    result = min(result, h_list[i] * n)

if result != max_val:
    print(result)
else:
    print("stay home")
