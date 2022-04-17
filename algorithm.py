class Solution:
    res = 0

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # 1. init
        self.res = 0

        # 2. dfs
        def dfs(node, val):
            if not node: return

            if not node.left and not node.right:
                self.res += int(f"{val}{node.val}", 2)
                return

            dfs(node.left, f"{val}{node.val}")
            dfs(node.right, f"{val}{node.val}")

        dfs(root, "")

        return self.res