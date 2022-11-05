n = int(input())

alpha_array = [chr(ord('a') + i) for i in range(0, 26)]
alpah_set = set(alpha_array)

for _ in range(n):
    s = [c for c in input().lower() if c in alpah_set]
    input_set = set(s)

    if len(input_set) == 26:
        print("pangram")
    else:
        print("missing", "".join(sorted(list(alpah_set - input_set))))
