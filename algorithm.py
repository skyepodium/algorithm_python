# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    a = []
    b = []
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # 1. init
        self.a = []
        self.b = []

        # 2. dfs
        def dfs(root, l):
            if root:
                if not root.left and not root.right:
                    l.append(root.val)
                dfs(root.left, l)
                dfs(root.right, l)

        dfs(root1, self.a)
        dfs(root2, self.b)

        return self.a == self.b

sl = Solution()

root1 = TreeNode(1)
root2 = TreeNode(1)

res = sl.leafSimilar(root1, root2)
print('res', res)