class Solution:
    def hasDuplicate(self, nums):
        z={}
        for i in nums:
            z[i] = z.get(i, 0) + 1
            
            if z[i] > 1:
                return True
        return False