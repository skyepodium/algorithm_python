class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # 1. init
        self.res = 0

        # 2. preorder
        def go(node, is_left):
            if not node:
                return

            if not node.left and not node.right and is_left:
                self.res += node.val

            go(node.left, True)
            go(node.right, False)

        go(root, False)

        return self.res