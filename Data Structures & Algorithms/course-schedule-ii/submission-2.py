class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        res = []
        graph = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        done = set()

        def dfs(node):

            if node in visited:
                return False
            if node in done: return True
            visited.add(node)
            for neigh in graph[node]:

                cap = dfs(neigh)
                if not cap: 
                    return False
            res.append(node)
            done.add(node)
            visited.remove(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res