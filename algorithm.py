# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            self.max = max(self.max, depth)
            if not node:
                return depth

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return self.max
