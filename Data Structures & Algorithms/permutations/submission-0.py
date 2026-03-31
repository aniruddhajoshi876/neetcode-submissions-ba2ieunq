class Solution:
    def permute(self, nums):

        res = []
        used = [False] * len(nums)
        subset = []

        def dfs(index):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):

                if used[i]:
                    continue
                
                subset.append(nums[i])
                used[i] = True
                dfs(i+1)
                subset.pop()
                used[i] = False
        dfs(0)
        return res

        