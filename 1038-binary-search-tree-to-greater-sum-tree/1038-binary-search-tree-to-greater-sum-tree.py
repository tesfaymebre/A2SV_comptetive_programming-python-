# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.pre_sum = 0
        
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            node.val += self.pre_sum
            self.pre_sum = node.val
            dfs(node.left)
            
        dfs(root)
        return root