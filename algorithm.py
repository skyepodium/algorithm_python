class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. init
        node = slow = fast = ListNode(None)
        node.next = head

        # 2. runner
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 3. delete
        slow.next = slow.next.next

        return node.next