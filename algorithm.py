class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("[^a-zA-Z]", " ", paragraph).lower()

        words = [word for word in paragraph.split() if word not in banned]

        count = collections.defaultdict(int)

        res = ""
        cnt = 0

        for word in words:
            count[word] += 1
            if count[word] > cnt:
                cnt = count[word]
                res = word

        return res