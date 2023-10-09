# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # 1. init
        self.res = 0

        # 2. dfs
        def dfs(node: TreeNode, path_sum: str):
            if not node:
                return

            if not node.left and not node.right:
                self.res += int(f"{path_sum}{node.val}", 2)

            dfs(node.left, f"{path_sum}{node.val}")
            dfs(node.right, f"{path_sum}{node.val}")

        dfs(root, "")

        return self.res
