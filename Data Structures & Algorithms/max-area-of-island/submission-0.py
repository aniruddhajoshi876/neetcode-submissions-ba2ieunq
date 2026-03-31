class Solution:
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        max_area = 0
        def dfs(r,c):
            
            if not (0<= r < rows and 0<= c < cols) or grid[r][c] == 0:
                return 0
            count = 1

            grid[r][c]=0
            for dr,dc in directions:
                count += dfs(r+dr,c+dc)
            return count
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    max_area = max(max_area, area)
        return max_area