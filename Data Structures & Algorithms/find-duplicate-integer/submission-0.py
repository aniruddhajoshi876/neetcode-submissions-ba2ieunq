class Solution:
    def findDuplicate(self, nums):
        fast=0
        slow=0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow2