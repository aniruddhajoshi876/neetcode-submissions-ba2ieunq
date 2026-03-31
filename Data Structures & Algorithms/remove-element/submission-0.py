class Solution:
    def removeElement(self, nums, val):
        seen = {val:0}
        for i in nums:
            if i == val:
                seen[val] += 1
        for i in range(seen[val]):
            nums.remove(val)
        return len(nums)      