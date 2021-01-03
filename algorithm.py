def solution(numbers):
    answer = []

    check = [False for _ in range(201)]

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                sum_value = numbers[i] + numbers[j]
                if not check[sum_value]:
                    check[sum_value] = True
                    answer.append(sum_value)

    answer.sort()

    return answer