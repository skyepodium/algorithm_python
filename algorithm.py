def solution(s, n):
    answer = ""
    for c in s:
        if c == " ":
            answer += c
        elif c.islower():
            n_ord = ord(c) + n
            answer += chr(n_ord - 26) if n_ord > ord('z') else chr(n_ord)
        else:
            n_ord = ord(c) + n
            answer += chr(n_ord - 26) if n_ord > ord('Z') else chr(n_ord)
    return answer

s = "AB"
n = 1
s = "a B z"
n = 4
res = solution(s, n)

print(res)

print(chr(97))