import re

def solution(files):
    # 1. init
    f_list = []

    # 2. split_file with regex
    def split_file(s):
        # 1) head
        head = re.search("[^0-9]+", s).group(0)

        # 2) number
        number = re.search("[0-9]{1,5}", s).group(0)

        return [head, number]

    # 3. loop
    for idx, f in enumerate(files):
        head, number = split_file(f)
        f_list.append([head, number, idx, f])

    # 4. sort
    f_list.sort(key=lambda x: (
        x[0].lower(),
        int(x[1]),
        x[2]
    ))

    return [x[3] for x in f_list]

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

res = solution(files)

print('res', res)

