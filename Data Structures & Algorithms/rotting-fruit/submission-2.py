class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        levels = 0
        queue = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue:
            wave = len(queue)
            rotted = False

            for _ in range(wave):
                r,c = queue.pop(0)
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if (0 <= nr < rows and 0<= nc < cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        rotted = True

            if rotted:
                levels += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return levels