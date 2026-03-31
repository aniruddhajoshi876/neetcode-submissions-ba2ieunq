class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        col = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        number = 0
        def dfs(r,c):

            if not (0 <= r < rows and 0 <= c < col) or grid[r][c] == '0':
                return
            
            grid[r][c] ='0'

            for dr,dc in directions:
                dfs(r+dr, c+dc)
        
        for r in range(rows):
            for c in range(col):
                if grid[r][c]=='1':
                    dfs(r,c)
                    number+=1
        return number