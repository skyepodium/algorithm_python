def solution(nums):
    # 0. init
    answer = 0

    # 1. sort
    nums.sort()

    # 2. prime
    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # 3 two pointer
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if is_prime(nums[i] + nums[j] + nums[k]):
                    answer += 1

    return answer