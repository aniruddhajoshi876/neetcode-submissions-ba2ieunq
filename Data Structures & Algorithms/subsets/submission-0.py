class Solution:
    def subsets(self, nums):
        res= []
        subset = []

        def dfs(index):
            if index >= len(nums):
                res.append(subset.copy())
                return
            #include element
            subset.append(nums[index])
            dfs(index+1)

            #exclude element
            subset.pop()
            dfs(index+1)
        dfs(0)
        return res