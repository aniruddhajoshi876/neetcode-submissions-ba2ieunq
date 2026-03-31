import heapq
class Solution:
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        min_heap = nums

        while len(min_heap) > k:
            heapq.heappop(min_heap)
        return min_heap[0]
