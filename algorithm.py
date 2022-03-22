class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # 1. exception
        if s1 == s2: return True

        # 2. loop
        for i in range(len(s1)):
            for j in range(i + 1, len(s1)):
                if s1[0:i] + s1[j] + s1[i+1:j] + s1[i] + s1[j+1:] == s2: return True

        return False
