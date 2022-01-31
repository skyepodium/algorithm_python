import re
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        return sum(['' == re.sub(f"[{allowed}]", '', w) for w in words])
