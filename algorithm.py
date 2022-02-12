class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. init
        slow = fast = head

        # 2. runner
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 3. exception
        if fast and fast.next:
            slow = slow.next

        return slow