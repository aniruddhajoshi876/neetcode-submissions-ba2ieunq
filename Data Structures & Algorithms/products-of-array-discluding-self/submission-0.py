class Solution:
    def productExceptSelf(self, nums):
        def exc_prefix(numbers):
            prefix = [1 for _ in range(len(numbers))]

            for i in range(1,len(numbers)):
                prefix[i] = prefix[i-1] * numbers[i-1]
            return prefix
        def exc_suffix(numbers):
            suffix = [1 for _ in range(len(numbers))]

            for i in range(len(numbers)-2,-1,-1):
                suffix[i] = suffix[i+1] * numbers[i+1]
            return suffix
        
        res = [1 for _ in range(len(nums))]
        i=0
        suffix = exc_suffix(nums)
        prefix = exc_prefix(nums)
        while i < len(res):
            res[i] = suffix[i] * prefix[i]
            i+=1
        return res