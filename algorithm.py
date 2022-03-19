class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26



sl = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
sentence = "leetcode"

res = sl.checkIfPangram(sentence)

print('res', res)