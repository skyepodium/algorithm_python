class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 1. init
        res = []
        
        # 2. exception
        if not root:
            return []
        
        # 3. dfs
        def dfs(node, stack):
            if not node:
                return
            
            if not node.left and not node.right:
                stack.append(str(node.val))
                res.append("->".join(stack))
                stack.pop()
                return
            
            stack.append(str(node.val))
            dfs(node.left, stack)
            stack.pop()
            
            stack.append(str(node.val))
            dfs(node.right, stack)
            stack.pop()
            
        dfs(root, [])
        
        return res
