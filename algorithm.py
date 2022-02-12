class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = []
        origin = num
        while num > 0:
            nums.append(str(num%10))
            num //= 10
        nums = nums[::-1]
        for i, val in enumerate(nums):
            if val == '6':
                print(i, val)
                return int("".join(nums[:i]) + "9" + "".join(nums[i+1:]))

        return origin