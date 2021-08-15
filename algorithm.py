def solution(s):
    return f"{min([int(x) for x in s.split(' ')])} {max([int(x) for x in s.split(' ')])}"