class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        total_sum = int("".join([str(x) for x in num])) + k

        return [int(x) for x in str(total_sum)]