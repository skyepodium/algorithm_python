class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 1. init
        res = []

        # 2. exception
        if not root:
            return res

        # 3. pre_order
        def pre_order(node):
            if not node:
                return

            res.append(node.val)
            pre_order(node.left)
            pre_order(node.right)

        pre_order(root)

        return res