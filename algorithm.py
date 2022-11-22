from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = int(-1e9)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 1. dfs
        def dfs(node):
            # 1) exception
            if not node:
                return 0

            # 2) recursion
            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))

            # 3) update
            self.res = max(self.res, l + r + node.val)

            # 4) return
            return max(l, r) + node.val

        dfs(root)
        return self.res

