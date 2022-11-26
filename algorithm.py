n = int(input())
s = input().split(" ")

check = [False] * (11)
st = []
val_list = [-int(1e10), int(1e10)]
res_list = ['', '']

def dfs(idx: int) -> None:
    if idx > n:

        for i, c in enumerate(s):
            if c == '<' and st[i] > st[i+1]:
                return
            if c == '>' and st[i] < st[i+1]:
                return
        base = 0
        for num in st:
            base = base * 10 + num
        if base > val_list[0]:
            val_list[0] = base
            res_list[0] = ''.join(map(str, st))
        if base < val_list[1]:
            val_list[1] = base
            res_list[1] = ''.join(map(str, st))
        return

    for i in range(10):
        if not check[i]:
            if st:
                if s[idx-1] == "<":
                    if st[-1] > i:
                        continue
                else:
                    if st[-1] < i:
                        continue

            check[i] = True
            st.append(i)
            dfs(idx + 1)
            st.pop()
            check[i] = False

dfs(0)

print(res_list[0])
print(res_list[1])
