class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        subset =[]
        candidates.sort()
        def dfs(index, sum):
            if sum == target:
                res.append(subset.copy())
                return
            if sum > target:
                return
            
            for i in range(index, len(candidates)):

                if i > index and candidates[i] == candidates[i-1]:
                    continue

                subset.append(candidates[i])
                dfs(i+1, sum+candidates[i])
                subset.pop()
        dfs(0,0)
        return res