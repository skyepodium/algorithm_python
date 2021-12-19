# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def go(node):
            if not node:
                return 0

            left_depth = go(node.left)
            right_depth = go(node.right)

            self.result = max(self.result, left_depth + right_depth)

            return max(left_depth, right_depth) + 1

        go(root)

        return self.result