class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        connected = 0
        def dfs(node):
            visited.add(node)
            
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                connected+=1
        return connected
                
