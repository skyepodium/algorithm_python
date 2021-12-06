class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        a_d = {}
        a_set = set()
        b_d = {}
        b_set = set()

        for a, b in zip(s, t):
            if a not in a_set:
                a_d[a] = b
                a_set.add(a)
            else:
                if a_d[a] != b:
                    return False

        for a, b in zip(s, t):
            if b not in b_set:
                b_d[b] = a
                b_set.add(b)
            else:
                if b_d[b] != a:
                    return False

        return True
