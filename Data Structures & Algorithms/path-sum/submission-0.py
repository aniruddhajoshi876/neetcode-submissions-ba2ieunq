# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        self.res=False
        def dfs(node, sum):
            if not node:
                return None
            
            sum+=node.val

            if sum == targetSum and not node.left and not node.right:
                self.res=True
                return True
            
            if dfs(node.left,sum):
                self.res=True
                return True

            if dfs(node.right, sum):
                self.res=True
                return True

            return False
        
        return dfs(root,0)

        