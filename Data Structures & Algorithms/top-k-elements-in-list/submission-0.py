class Solution:
    def topKFrequent(self, nums, k):
        count={}
        res=[]
        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        for _ in range(k):
            z=max(count, key=count.get)
            res.append(z)
            count[z]=0
        return res