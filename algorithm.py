class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # 1. init
        res = 0

        # 2. sort
        skill.sort()

        # 3. loop
        l, r = 0, len(skill) - 1
        sum_skill = skill[l] + skill[r]
        while l < r:
            if skill[l] + skill[r] != sum_skill:
                return -1
            res += skill[l] * skill[r]
            l += 1
            r -= 1

        return res