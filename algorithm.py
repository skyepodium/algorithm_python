import re

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # 1. over 8 characters
        if len(password) < 8:
            return False

        # 2. one lowercase letter
        if password.upper() == password:
            return False

        # 3. one uppercase letter
        if password.lower() == password:
            return False

        # 4. one digit
        if len(re.sub("[0-9]", '', password)) == len(password):
            return False

        # 5. one special character
        if len(re.sub("[!@#$%^&*()\\-+]", '', password)) == len(password):
            return False

        # 6. same character
        for i in range(len(password) - 1):
            if password[i] == password[i+1]:
                return False

        return True

sl = Solution()
password = "IloveLe3tcode!"
password = "Me+You--IsMyDream"
password = "1aB!"
password = "aabab12!Aab"
password = "-Aa1a1a1"
res = sl.strongPasswordCheckerII(password)

print('res', res)
