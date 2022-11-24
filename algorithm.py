while True:
    s = input()
    if s[0] == "#":
        break

    c, s = s[0], s[2:]
    print(f"{c} {s.lower().count(c)}")