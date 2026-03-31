import heapq
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        queue = deque()
        time = 0
        maxheap = [-ct for ct in count.values()]
        heapq.heapify(maxheap)
        while maxheap or queue:
            time+=1
            if maxheap:
                c = 1 + heapq.heappop(maxheap)
                if c:
                    queue.append((c, time+n))
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap,queue.popleft()[0])
        return time