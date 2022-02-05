from typing import List, Optional

from Cython.Compiler.ExprNodes import ListNode
from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1. init
        pq = []
        head = node = None
        l = []

        # 2. make pq
        for idx, node in enumerate(lists):
            cur = []
            while node:
                cur.append(node.val)
                node = node.next
            l.append(cur)
            if len(cur) > 0:
                heappush(pq, (cur[0], 0, idx))

        # 3. search
        while pq:
            val, inner_idx, list_idx = heappop(pq)
            if inner_idx < len(l[list_idx]) - 1:
                heappush(pq, (l[list_idx][inner_idx + 1], inner_idx + 1, list_idx))

            if node:
                node.next = ListNode(val, None)
                node = node.next
            else:
                node = ListNode(val, None)
                head = node

        return head