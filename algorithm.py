class Solution:
    def trap(self, height: list[int]) -> int:

        result = 0;

        # 1. 왼쪽, 오른쪽 최대 높이 저장할 변수 생성
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]

        while l <= r:
            # 2. 투 포인터 왼쪽, 오른쪽 최대값 갱신
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            # 3. 최대 높이를 향해 투 포인터 이동
            if left_max <= right_max:
                result += left_max - height[l]
                l += 1
            else:
                result += right_max - height[r]
                r -= 1

        return result


sl = Solution()
height = [4,2,0,3,2,5]
res = sl.trap(height)

print(res)