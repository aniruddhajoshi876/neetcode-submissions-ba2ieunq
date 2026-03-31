class Solution:
    def islandsAndTreasure(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        directions = [(0,1),(-1,0),(1,0),(0,-1)]

        queue = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        while queue:

            r,c = queue.pop(0)

            for dr,dc in directions:
                nr,nc=r+dr,c+dc

                if (0<=nr<rows and 0<=nc<cols) and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
