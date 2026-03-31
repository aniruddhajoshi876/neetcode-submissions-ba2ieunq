from math import sqrt
import heapq
class Solution:
    def kClosest(self, points, k):
        def distance(x,y):
            return (sqrt((x**2)+(y**2)), (x,y))

        heap = []
        heapq.heapify(heap)

        for x,y in points:
            heapq.heappush(heap, distance(x,y))
        res = []
        while len(res) < k:
            dist, coord = heapq.heappop(heap)
            res.append(coord)
        return res  