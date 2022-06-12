for k in range(127):
    res = "".join(chr(ord(c) ^ k) for c in "Fpvgpa8'M,m&!s,!")
    print('k', k, 'res', res)
