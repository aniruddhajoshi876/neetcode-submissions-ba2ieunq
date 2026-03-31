class Solution:
    def searchMatrix(self, matrix, target):
        def search(self, nums, target):

            l=0
            r=len(nums)-1

            while l <= r:
                mid = (l+r)//2

                if nums[mid] < target:
                    l = mid+1
                elif nums[mid] > target:
                    r = mid-1
                else:
                    return True
            return False
        l=0
        r=len(matrix)-1
        
        while l<=r:
            mid = (l+r)//2

            if abs(r-l) <= 1:
                return search(self,matrix[l], target) or search(self,matrix[r], target)
            elif matrix[mid][0] > target:
                r= mid
            
            elif matrix[mid][0] < target:
                l = mid
            
            
            elif matrix[mid][0] == target:
                return True
        return False