class Solution:
    def rob(self, nums):
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0  
        if len(nums) == 2:
            return max(nums[0], nums[1])  
        dp = [0]*(n-1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        dp2 = [0]*(n-1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])

        for i in range(2, n-1):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        
        for i in range(2, n-1):
            dp2[i] = max(nums[i+1]+dp2[i-2], dp2[i-1])
        
        return max(dp[n-2], dp2[n-2])
