class Solution:
    def stoneGame(self, piles) -> bool:
        l = 0
        r = len(piles) - 1

        def get_big(l_idx, r_idx):
            if r_idx - l_idx < 3:
                return simple_small(l_idx, r_idx)

            left_val = piles[l_idx] - max(piles[l_idx + 1], piles[r_idx])
            right_val = piles[r_idx] - max(piles[l_idx], piles[r_idx - 1])

            if left_val > right_val:
                return 0
            elif left_val < right_val:
                return 1
            else:
                return get_big(l_idx + 1, r_idx -1)

        def simple_big(l_idx, r_idx):
            return 0 if piles[l_idx] > piles[r_idx] else 1

        def simple_small(l_idx, r_idx):
            return 0 if piles[l_idx] < piles[r_idx] else 1

        alex = 0
        lee = 0
        cnt = 0
        while l <= r:
            if r - l >= 3:
                idx = get_big(l, r)
            else:
                idx = simple_big(l, r)

            val = piles[l] if idx == 0 else piles[r]

            if cnt % 2 == 0:
                alex += val
            else:
                lee += val

            if idx == 0:
                l += 1
            else:
                r -= 1

            cnt += 1
            print('idx', idx)
            print('alex', alex, 'lee', lee)
        return alex > lee

s = Solution()

p = [5, 3, 4, 5]
p = [3,2,10,4]
p = [1,4,10,8,3,2,4,1]
# p = [3, 7, 2, 3]
# p = [6,9,4,3,9,8]
res = s.stoneGame(p)
print('res', res)
