class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. init
        fast = slow = head
        s = []

        # 2. runner
        while fast and fast.next:
            s.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # 3. stack
        res = slow.next
        while s:
            res = ListNode(s.pop(), res)

        return res