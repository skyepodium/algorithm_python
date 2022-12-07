# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    res = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # 1. init
        self.res = 0

        # 2. traverse
        def dfs(node):
            if not node:
                return

            if low <= node.val <= high:
                self.res += node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.res