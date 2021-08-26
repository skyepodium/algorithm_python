class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 1. init
        res = []
        
        # 2. exception
        if not root:
            return res
        
        # 3. dfs
        def dfs(node, val, stack):
            if not node:
                return
            
            if not node.left and not node.right:
                if val + node.val == targetSum:
                    stack.append(node.val)
                    res.append(stack[:])
                    stack.pop()
                    return
            
            
            stack.append(node.val)
            dfs(node.left, val + node.val, stack)
            stack.pop()
            
            stack.append(node.val)
            dfs(node.right, val + node.val, stack)
            stack.pop()
        
        dfs(root, 0, [])
        
        return res
            
