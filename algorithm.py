import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:

        d = collections.defaultdict(int)

        for c in s:
            d[c] += 1

        result = 0
        max_odd_cnt = 0
        for val in d.values():
            if val % 2 == 0:
                result += val
            else:
                max_odd_cnt = max(max_odd_cnt, val)
                if val - 1 >= 2:
                    result += val - 1

        if max_odd_cnt >= 1:
            result += 1

        return result

sl = Solution()

s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
s = "c"
res = sl.longestPalindrome(s)

print('res', res)