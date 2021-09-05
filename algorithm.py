class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 1. init
        res = []

        # 2. exception
        if not root:
            return res

        # 3. post_order
        def post_order(node):
            if not node:
                return

            post_order(node.left)
            post_order(node.right)
            res.append(node.val)

        post_order(root)

        return res