import heapq
class Solution:
    def minCostConnectPoints(self, points):
        
        n = len(points)
        graph ={i: [] for i in range(n)}

        for i in range(n):
            
            x1,y1 = points[i]

            for j in range(i+1, n):
                x2,y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                graph[i].append((cost, j))
                graph[j].append((cost, i))
        
        pq = [(0,0)]
        visited = set()
        res = 0
        while pq:

            cost, node = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)
            res+=cost

            for neighcost, neigh in graph[node]:
                if neigh not in visited:
                    heapq.heappush(pq,(neighcost, neigh))
        return res
