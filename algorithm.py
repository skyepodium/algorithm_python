# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        root = node = ListNode(0)

        while head:
            if head.val != val:
                node.next = ListNode(head.val, None)
                node = node.next
            head = head.next

        return root.next