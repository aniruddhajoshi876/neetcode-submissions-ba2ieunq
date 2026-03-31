import heapq
class Solution:
    def lastStoneWeight(self, stones):
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            a = heapq.heappop(max_heap)
            b = heapq.heappop(max_heap)
            if abs(a-b) != 0:
                heapq.heappush(max_heap, -abs(a-b))
        if not max_heap: 
            return 0 
        return -max_heap[0]