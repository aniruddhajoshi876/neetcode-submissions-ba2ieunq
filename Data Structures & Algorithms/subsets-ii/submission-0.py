class Solution:
    def subsetsWithDup(self, nums):
        res = []
        subset = []
        nums.sort()
        def dfs(index):
            res.append(subset.copy())
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue

                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
                
        dfs(0)
        return res