class Solution:
    def findRedundantConnection(self, edges):

        n = max(max(a,b) for a,b in edges)
        graph=[[] for _ in range(n+1)]

        visited = set()

        def dfs(node, parent):
            if node == target:
                return True
            visited.add(node)
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if neigh not in visited and dfs(neigh,node):
                    return True
            return False

        for start,target in edges:
            if dfs(start, -1):
                return [start, target]
            visited.clear()
            graph[start].append(target)
            graph[target].append(start)