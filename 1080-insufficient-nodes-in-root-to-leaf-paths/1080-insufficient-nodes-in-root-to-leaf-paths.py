# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node,total):
            if not node:
                return False
            
            total += node.val
            
            if not node.left and not node.right:
                return total >= limit
                    
            left = dfs(node.left,total) 
            right = dfs(node.right, total)
            
            if not left:
                node.left = None
                
            if not right:
                node.right = None
            
            return left or right
                
        result = dfs(root,0)
        return root if result else None