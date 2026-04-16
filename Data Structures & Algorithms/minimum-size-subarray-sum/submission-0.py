class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        res = float("INF")
        window = []
        for end in range(len(nums)):
            while sum(window) >= target:
                
                window.pop(0)
                start+=1
                if sum(window) >= target:
                    res=min(res, len(window))
            window.append(nums[end])
        
        if res == float("INF"):
            return 0
        return res