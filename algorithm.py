class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        slow = fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False