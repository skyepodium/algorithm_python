class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # 1. init
        l = 0
        c = head
        while c:
            c = c.next
            l += 1

        # 2. exception
        if n == 1 and l == 1: return None

        # 3. loop
        idx = l - n
        i = 0

        node = pointer = ListNode(None)
        node.next = head
        while pointer:

            if i >= idx:
                pointer.next = pointer.next.next
                break

            pointer = pointer.next
            i += 1

        return node.next