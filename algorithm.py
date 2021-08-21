# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 1. init
        l1_number = ""
        l2_number = ""

        # 2. loop
        while l1:
            l1_number += str(l1.val)
            l1 = l1.next

        while l2:
            l2_number += str(l2.val)
            l2 = l2.next

        # 3. add
        res = str(int(l1_number[::-1]) + int(l2_number[::-1]))

        result = None
        for i in res:
            result, result.next = ListNode(i, None), result

        return result

