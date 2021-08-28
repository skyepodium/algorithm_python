class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head

        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return root