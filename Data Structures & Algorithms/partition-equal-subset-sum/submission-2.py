class Solution:
    def canPartition(self, nums):
        target = sum(nums)//2
        if sum(nums)%2 ==1: return False 
        dp = [False]*(target+1)
        dp[0]=True

        for num in nums:
            j=target
            while j>=num:
                dp[j] = dp[j] or dp[j-num]
                j-=1
        return dp[target]