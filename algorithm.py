from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 0. exception
        if not root:
            return 0

        # 1. init
        q = deque()
        q.append((root, 1))

        # 2. BFS
        while q:
            node, step = q.popleft()

            l = node.left
            r = node.right
            if not l and not r:
                return step

            for next_node in [l, r]:
                if not next_node: continue
                q.append((next_node, step + 1))

        return 0