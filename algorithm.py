for k in range(250):
    res = "".join(chr(ord(c)^k) for c in "Fpvgpa8'M,m&!s,!")
    print('res', res)
