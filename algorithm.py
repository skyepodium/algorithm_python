class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 1. exception
        if not root:
            return []

        # 2. init
        res = []

        # 3. inorder
        def go(node):
            if not node:
                return

            go(node.left)
            res.append(node.val)
            go(node.right)

        go(root)

        return res