# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node, prev):
            nonlocal ans
            if not node: return 0
            
            left =  dfs(node.left, node.val)
            right = dfs(node.right, node.val)
            ans = max(ans, left+right)
            
            if prev== node.val:
                return max(left, right) + 1
            else:
                return 0 
        
        dfs(root,float("inf"))
        return ans