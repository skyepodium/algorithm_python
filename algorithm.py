# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # 1. init
        self.res = True
        self.val = root.val

        # 2. dfs
        def dfs(node):
            if not node:
                return

            if node.val != self.val:
                self.res = False

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.res