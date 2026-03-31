class Solution:
    def maxProduct(self, nums):
        dp = [0]*len(nums)
        max_p=min_p=dp[0]=nums[0]
        res=nums[0]
        for i in range(1, len(nums)):
            
            prev_max = max_p
            max_p = max(nums[i], nums[i]*prev_max, min_p*nums[i])
            min_p=min(nums[i], nums[i]*prev_max, nums[i]*min_p)
            res=max(res,max_p)
        return res
