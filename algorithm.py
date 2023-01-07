class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1. init
        banned_set = set(banned)
        paragraph = re.sub('[^a-zA-z ]', ' ', paragraph.lower())

        # 2. loop
        c = Counter([p for p in paragraph.split() if p not in banned_set])
        return c.most_common()[0][0]