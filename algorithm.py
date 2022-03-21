class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # 1. init
        d = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        res = 0

        # 2. loop
        for i in items:
            if i[d[ruleKey]] == ruleValue:
                res += 1

        return res