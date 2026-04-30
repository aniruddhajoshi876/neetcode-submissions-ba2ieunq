# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1, root2):
        self.res = None
        if not root2:
            return root1
        if not root1:
            return root2
        def dfs(node1, node2):

            if not node1 and not node2:
                return None
            
            if not node1:
                return node2
            if not node2:
                return node1
            if node1 and node2:
                root = TreeNode(node1.val + node2.val)
            if node1 and not node2:
                root= TreeNode(node1.val)
            if not node1 and node2:
                root= TreeNode(node2.val)

            if not self.res:
                self.res = root
            

            root.left = dfs(node1.left, node2.left)
            root.right = dfs(node1.right, node2.right)

           
            
            return root
        
        dfs(root1, root2)

        return self.res   

            





        