n = int(input())

def can_palindrome(s):
    l, r = 0, len(s) - 1
    count = 0
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif s[l] != s[r]:
            if count == 0:
                count += 1
                l += 1
            else:
                break
    return 1 if l >= r else 2

def check_palindrome(s):
    if s == s[::-1]:
        return 0

    return 1 if can_palindrome(s) == 1 or can_palindrome(s[::-1]) == 1 else 2

for _ in range(n):
    s = input()
    print(check_palindrome(s))
