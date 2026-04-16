class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        res = float("INF")
        window = []
        cur_sum = 0
        for end in range(len(nums)):
            
            cur_sum+=nums[end]
            
            while cur_sum >= target:
                res=min(res, end-start+1)
                cur_sum-=nums[start]
                start+=1
                
            
        
        if res == float("INF"):
            return 0
        return res
