class Solution:
    def topKFrequent(self, nums, k):
        count={}
        res=[]
        for i in nums:
            count[i] = 1 + count.get(i,0)
        freq = [[] for _ in range(len(nums)+1)] 
        for n,c in count.items():
            freq[c].append(n)

        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
            if len(res) == k:
                return res
