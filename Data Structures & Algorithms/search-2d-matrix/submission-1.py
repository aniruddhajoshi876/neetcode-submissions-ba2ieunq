class Solution:
    def searchMatrix(self, matrix, target):
        l=0
        r=len(matrix)-1
        
        while l<=r:
            mid = (l+r)//2

            if abs(r-l) <= 1:
                return target in matrix[l] or target in matrix[r]
            elif matrix[mid][0] > target:
                r= mid
            
            elif matrix[mid][0] < target:
                l = mid
            
            
            elif matrix[mid][0] == target:
                return True
        return False
