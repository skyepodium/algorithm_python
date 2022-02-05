class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1. init
        head = node = None
        nums = []

        # 2. loop
        for c in lists:
            while c:
                nums.append(c.val)
                c = c.next

        # 3. sort
        nums.sort()

        # 4. loop
        for n in nums:
            if node:
                node.next = ListNode(n, None)
                node = node.next
            else:
                head = node = ListNode(n, None)

        return head