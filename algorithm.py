class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1. exception
        if not root:
            return 0

        # 2. init
        self.res = 0

        # 3. dfs
        def dfs(node, cnt):
            if not node:
                return

            if not node.left and not node.right:
                self.res = max(self.res, cnt)
                return

            dfs(node.left, cnt + 1)
            dfs(node.right, cnt + 1)

        dfs(root, 1)

        return self.res   
