class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 1. init
        d = {}
        e = set()
        p_list = [x for x in pattern]
        s_list = s.split(" ")

        # 2. exception
        if len(p_list) != len(s_list):
            return False

        # 3. loop
        for a, b in zip(p_list, s_list):
            if a in d:
                if d[a] != b:
                    return False
            else:
                d[a] = b
                if b in e:
                    return False
                e.add(b)

        return True
