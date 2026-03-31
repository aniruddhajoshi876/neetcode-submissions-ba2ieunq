class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[b].append(a)

        visited = set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for neigh in graph[node]:
                cap = dfs(neigh)
                if not cap:
                    return False
            visited.remove(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True