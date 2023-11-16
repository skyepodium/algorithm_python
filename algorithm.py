from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # 1. init
        unique_emails = set()

        # 2. loop
        for email in emails:
            local, domain = email.split("@")

            if "+" in local:
                local = local[:local.index("+")]

            local = local.replace(".", "")

            email_result = f"{local}@{domain}"
            if email_result not in unique_emails:
                unique_emails.add(email_result)

        return len(unique_emails)


emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
sl = Solution()
print(sl.numUniqueEmails(emails))
