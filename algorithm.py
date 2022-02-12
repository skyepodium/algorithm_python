class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. init
        slow = fast = head

        # 2. runner
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow