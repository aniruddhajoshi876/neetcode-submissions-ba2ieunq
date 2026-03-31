# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    good = 0 
    def goodNodes(self, root, max_val=-9999):
        if not root:
            return 0
        
        if max_val <= root.val:
            self.good+=1        
        max_val = max(max_val, root.val)
        self.goodNodes(root.left,max_val)
        self.goodNodes(root.right, max_val)
        return self.good

