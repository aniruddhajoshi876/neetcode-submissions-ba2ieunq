class Solution:
    def longestConsecutive(self, nums):
        numbers = set(nums)
        res = 0

        for i in nums:
            if (i-1) not in numbers:
                length = 1
                while (i+length) in numbers:
                    length +=1
                res = max(res, length)
        return res
        