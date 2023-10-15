def solution(num_list):
    result = -1

    for idx, num in enumerate(num_list):
        if num < 0:
            return idx

    return result
