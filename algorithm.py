class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        result = []
        size = len(nums)

        # 1. 자기 자신을 제외한 왼쪽 곱셈을 저장한다.
        base = 1
        for i in range(0, size):
            result.append(base)
            base *= nums[i]

        # 2. 1번 결과에 자기 자시을 제외한 오른쪽 곰셉을 곱해준다.
        base = 1
        for i in range(size - 1, -1, -1):
            result[i] = result[i] * base
            base *= nums[i]

        return result


sl = Solution()

nums = [1, 2, 3, 4]

res = sl.productExceptSelf(nums)

print('res', res)