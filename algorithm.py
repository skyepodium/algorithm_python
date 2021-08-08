class Solution:
    def longestPalindrome(self, s: str) -> str:

        result = ""

        # 1. 예외 처리
        if len(s) < 2 or s == s[::-1]:
            return s

        # 2. 투 포인터
        def expand(l, r):
            while l >= 0 and r <= len(s) and s[l] == s[r-1]:
                l -= 1
                r += 1

            # 현재 투포인터가 있는 위치가 팰린드롬이 아니거나
            # 인덱스를 넘어갔기 때문에 바로 이전 상태로 돌아간다.
            # 처음부터 팰린드롬이 아닌경우, 홀수개는 문자 1개, 짝수개는 빈문자열을 반환한다.
            return s[l+1: r-1]

        # 3. 한개씩 중심 탐색
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i+1),
                         expand(i, i+2),
                         key=len
                         )

        return result

sl = Solution()

s = "abb"

res = sl.longestPalindrome(s)

print('res', res)