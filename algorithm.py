def solution(numbers):
    # 1. init
    res = []

    # 2. num_to_bit
    def num_to_bit(n):
        result = ""
        while n > 0:
            if n & 1 == 1: val = "1"
            else: val = "0"
            result += val
            n //= 2
        return result[::-1]

    def bit_to_num(num):
        result = 0
        base = 0
        n = len(num)
        for i in reversed(range(n)):
            result += int(num[i]) * (2 ** base)
            base += 1
        return result

    def check_num(num):
        # 1. even
        if num & 1 == 0:
            return num + 1
        else:
            one_pos = -1
            zero_pos = -1
            bit_num = num_to_bit(num)
            n = len(bit_num)
            for i in range(n):
                if bit_num[i] == "1" and one_pos == -1:
                    one_pos = i
                if bit_num[i] == "0" and zero_pos == -1:
                    zero_pos = i
            if one_pos != -1:
                bit_num = bit_num[:one_pos] + "0" + bit_num[one_pos+1:]
            else:
                bit_num = "1"
            if zero_pos != -1:
                bit_num = bit_num[:zero_pos] + "1" + bit_num[zero_pos+1:]
            else:
                bit_num = "1" + bit_num
            return bit_to_num(bit_num)

    return [check_num(x) for x in numbers]



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [2, 7]
res = solution(numbers)

print('res', res)