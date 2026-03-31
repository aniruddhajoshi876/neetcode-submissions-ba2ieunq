# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        self.isbalanced = True
        if not root: return True
        def find_height(root):
            if not root: return 0

            left,right = find_height(root.left), find_height(root.right)
            if abs(left - right) > 1:
                self.isbalanced = False
            height = max(left, right) +1
            return height
        
        find_height(root)
        return self.isbalanced
        