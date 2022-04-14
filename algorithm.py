class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return
        
        if root.val == val: return root
        
        return self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val)
