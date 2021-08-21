# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. init
        rev = None
        slow = fast = head

        # 2. runnter
        while fast and fast.next:
            fast = fast.next.next

            rev, rev.next, slow = slow, rev, slow.next

        # if length is a odd number, go one step forward
        if fast:
            slow = slow.next

        # 3. palindrome check
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev