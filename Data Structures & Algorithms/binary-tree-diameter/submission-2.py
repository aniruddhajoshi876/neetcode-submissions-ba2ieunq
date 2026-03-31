# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def find_height(root):
            height = 0
            if not root: return 0
            
            left,right = find_height(root.left), find_height(root.right)
            height = max(left, right)+1
            self.diameter = max(self.diameter, left + right )
            return height
        find_height(root)
        return self.diameter