t = int(input())

res = 0
for i in range(t):
    s = input()
    st = []

    for c in s:
        if not st:
            st.append(c)
        else:
            if st[-1] == c:
                st.pop()
            else:
                st.append(c)

    if not st:
        res += 1

print(res)