class Solution:
    def validTree(self, n, edges):
        graph= [[] for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited=set()

        def dfs(node, parent):
            
            visited.add(node)
            for neigh in graph[node]:
                if parent == neigh:
                    continue
                if neigh in visited:
                    return False
                if not dfs(neigh, node):
                    return False
            return True
        
        
        if not dfs(0,-1) or len(visited) != n:
            return False
        return True