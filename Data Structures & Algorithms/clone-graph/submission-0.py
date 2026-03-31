"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node):

        if not node:
            return None
        clones = {}
        def dfs(node, clones):
            if node in clones:
                return clones[node]
            clones[node] = Node(node.val, [])
            for neigh in node.neighbors:
                neighbor = dfs(neigh, clones)
                clones[node].neighbors.append(neighbor)
            
            return clones[node]
        
        
        return dfs(node, clones)