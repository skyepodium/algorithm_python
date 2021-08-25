# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def hasPathSum(root, targetSum) -> bool:
        # 1. exception
        if not root:
            return False

        global is_exist
        is_exist = False

        # 2. dfs
        def dfs(node, val):
            if not node:
                return

            if node and not node.left and not node.right and val + node.val == targetSum:
                global is_exist
                is_exist = True
                return

            if node.left:
                dfs(node.left, val + node.val)

            if node.right:
                dfs(node.right, val + node.val)

        dfs(root, 0)

        return is_exist



root = TreeNode(1, None, None)
left = TreeNode(2, None, None)
root.left = left

sl = Solution

res = sl.hasPathSum(root, 1)

print('res', res)