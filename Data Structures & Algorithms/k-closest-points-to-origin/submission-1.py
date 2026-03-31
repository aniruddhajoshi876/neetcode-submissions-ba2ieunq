from math import sqrt
import heapq
class Solution:
    def kClosest(self, points, k):
        def distance(x,y):
            return sqrt((x**2)+(y**2))

        heap = []
        heapq.heapify(heap)

        for i in range(k):
            x,y=points[i]
            heapq.heappush(heap, (-distance(x,y),(x,y)))
        for x,y in points[k::]:
            if distance(x,y) < -heap[0][0]:
                heapq.heappushpop(heap,(-distance(x,y),(x,y)))

        return [coord for (_,coord) in heap]