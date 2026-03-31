# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root, min=-float('inf'), max=float('inf')):
        if not root:
            return True
        
        if not (min < root.val < max):
            return False

        return self.isValidBST(root.left,min,max=root.val) and self.isValidBST(root.right,min=root.val,max=max)

        