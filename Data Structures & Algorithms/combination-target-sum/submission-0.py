class Solution:
    def combinationSum(self, nums, target):
        res = []
        sub = []
        def dfs(index, sum):
            print(sub)
            if target == sum:
                res.append(sub.copy())
                return
            if sum > target:
                return
            
            if  sum < target and len(nums) == index:
                return
            
            #add current index
            sub.append(nums[index])
            dfs(index, sum + nums[index])
            

            #skip current index
            sub.pop()
            dfs(index+1, sum)
        dfs(0,0)
        return res