def solution(numbers):
    # 1. init
    res = []

    # 2. loop
    for n in numbers:
        val = 0
        # 1) even
        if n % 2 == 0:
            val = n + 1
        # 2) odd
        else:
            bin_num = "{0:b}".format(n)
            bin_num_len = len(bin_num)
            # 2-1) find lowest zero index
            idx = bin_num.rfind('0')

            # 2-2) zero not exist
            if idx == -1:
                idx = bin_num_len - 1

            # 2-3) zero exist
            else:
                idx = bin_num_len - idx - 2

            val = n + (1 << idx)

        res.append(val)

    return res

numbers = [2, 7, 9]

res = solution(numbers)

print('res', res)
