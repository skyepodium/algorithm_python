import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        d = collections.defaultdict(int)
        idx = 0
        res_list = []
        for word in strs:
            val = "".join(sorted(word))
            if val in d:
                cur_idx = d[val]
                res_list[cur_idx].append(word)
            else:
                d[val] = idx
                res_list.append([word])
                idx += 1

        return res_list

s = Solution()

ss = ["eat","tea","tan","ate","nat","bat"]
res = s.groupAnagrams(ss)

print('res', res)