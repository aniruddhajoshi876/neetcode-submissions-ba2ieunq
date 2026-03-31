# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def buildTree(self, preorder, inorder):
        self.pre_index = 0
        index = {}
        for i in preorder:
            index[i] = inorder.index(i)
        
        def build(l,r):
            if l > r:
                return None
            
            mid = index[preorder[self.pre_index]]
            self.pre_index += 1
            root = TreeNode(inorder[mid])
            root.left = build(l, mid-1)
            root.right = build(mid+1, r)

            return root
        
        return build(0, len(inorder)-1)