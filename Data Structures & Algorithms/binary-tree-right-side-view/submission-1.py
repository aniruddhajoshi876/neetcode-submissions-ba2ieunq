# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root):
        if not root: return []
        queue = [root]
        z=[]
        while queue:
            q = len(queue)
            level = []
            for _ in range(q):
                node=queue.pop(0)
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            z.append(level[-1])
        return z