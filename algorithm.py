from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. init
        fast = slow = head

        # 2. runner
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        # 3. move
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next

        return fast
