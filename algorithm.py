# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 1. exception
        if not root:
            return False

        # 2. init
        res = []

        # 3. dfs
        def dfs(node, val):
            if not node:
                return

            if not node.left and not node.right and val + node.val == targetSum:
                res.append(True)
                return

            if node.left:
                dfs(node.left, val + node.val)

            if node.right:
                dfs(node.right, val + node.val)

        dfs(root, 0)

        return any(res)