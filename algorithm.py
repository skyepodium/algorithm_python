class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # 1. 리스트 컴프리헨션으로 (인덱스, 값) 튜플 리스트 생성
        num_list = [(idx, num) for idx, num in enumerate(nums)]

        # 2. 값 기준 정렬
        num_list.sort(key=lambda x: x[1])

        # 3. 투포인터
        l = 0
        r = len(num_list) - 1

        while l < r:
            sum_val = num_list[l][1] + num_list[r][1]
            # 1) 값이 크면 오른쪽 포인터 왼쪽으로
            if sum_val > target:
                r -= 1
            # 2) 값이 작으면 왼쪽 포인터 오른쪽으로
            elif sum_val < target:
                l += 1
            # 3) 값이 같으면, 인덱스 반환
            else:
                return num_list[l][0], num_list[r][0]

sl = Solution()

nums = [3, 2, 4]
target = 6

res = sl.twoSum(nums, target)

print('res', res)