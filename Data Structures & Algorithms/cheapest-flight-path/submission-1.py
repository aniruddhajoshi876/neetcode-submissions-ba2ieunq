import heapq
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = {i: [] for i in range(n)}

        for start,end,cost in flights:
            graph[start].append((end,cost))
        
        distances = [[float('inf')]*(k+2) for _ in range(n)]

        distances[src][0] = 0

        pq = [(0,src, 0)]

        while pq:
            cost, city, num_flights = heapq.heappop(pq)

            if dst == city:
                return cost
            
            if num_flights == k+1:
                continue

            #if cost > distances[city][num_flights]:
                #continue

            for neigh, neighCost in graph[city]:
                new_cost = cost + neighCost
                if new_cost < distances[neigh][num_flights]:
                    distances[neigh][num_flights] = new_cost
                    heapq.heappush(pq, (new_cost,neigh, num_flights + 1))
        return -1
    