import heapq
class Solution:
    def networkDelayTime(self, times, n, k):
        graph= {node: [] for node in range(n+1)}
        for start, end, weight in times:
            graph[start].append((end,weight))
        
        distances = {node: float("inf") for node in graph.keys()}
        distances[k] = 0
        distances[0] = -1

        pq = [(0,k)]
        
        while pq:
            cur_dist, node = heapq.heappop(pq)

            if cur_dist > distances[node]:
                continue

            for neigh,weight in graph[node]:
                new_dist = cur_dist + weight

                if new_dist < distances[neigh]:
                    distances[neigh] = new_dist
                    heapq.heappush(pq, (new_dist, neigh))
        
        if max(distances.values()) != float('inf'):
            return max(distances.values())
        return -1