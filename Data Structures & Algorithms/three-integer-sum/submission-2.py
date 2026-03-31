class Solution:
    def threeSum(self, nums):
        nums.sort()
        triplet = []
        for i in range(len(nums)-1):
            j=i+1
            k=len(nums)-1
            target = -nums[i]
            while j < k:
                z=nums[j] + nums[k]
                if z > target:
                    k-=1
                elif z < target:
                    j+=1
                else:
                    triplet.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
        return list(set(tuple(row) for row in triplet))