# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k):
        self.count = 1
        def inorder(root):
            if not root:
                return None

            left = inorder(root.left)
            if left is not None:
                return left
            

            if self.count == k:
                return root.val
            self.count+=1

            right = inorder(root.right)
            if right is not None:
                return right
            

        return inorder(root)