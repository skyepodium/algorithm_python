class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([x.capitalize() if len(x) > 2 else x.lower() for x in title.split(" ")])