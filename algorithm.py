# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        res = node = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum_val = 0
            if l1:
                sum_val += l1.val
                l1 = l1.next

            if l2:
                sum_val += l2.val
                l2 = l2.next

            carry, val = divmod(sum_val + carry, 10)

            node.next = ListNode(val)
            node = node.next

        return res.next