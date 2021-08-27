from collections import Counter

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        d = Counter(moves)
        
        return d["U"] == d["D"] and d["L"] == d["R"]
