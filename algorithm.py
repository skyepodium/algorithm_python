def solution(nums):
    # 1. init
    answer = 0

    # 2. max_val
    max_int = max(nums) * 3
    d = [True for _ in range(max_int + 1)]

    # 3. eratos
    def eratos():
        for i in range(2, max_int + 1):
            for j in range(i+i, max_int+1, i):
                if d[j]:
                    d[j] = False

    eratos()

    # 4. nested loop
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if d[nums[i] + nums[j] + nums[k]]:
                    answer += 1

    return answer