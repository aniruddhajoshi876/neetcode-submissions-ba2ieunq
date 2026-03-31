class Solution:
    def maxArea(self, heights):
        max_area=0
        l=0
        r=len(heights)-1

        while l < r:
            height = min(heights[l], heights[r])

            area= height *(abs(l-r))
            max_area = max(max_area, area)
            
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] >= heights[r]:
                r-=1
        return max_area
            
        