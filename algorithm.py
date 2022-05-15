from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # 1. init
        self.d = 0
        self.res = 0

        # 2. dfs
        def dfs(node, depth):
            if depth == self.d:
                self.res += node.val

            if depth > self.d:
                self.d = depth
                self.res = node.val

            for n_node in [node.left, node.right]:
                if not n_node: continue
                dfs(n_node, depth + 1)

        dfs(root, 0)

        return self.res
