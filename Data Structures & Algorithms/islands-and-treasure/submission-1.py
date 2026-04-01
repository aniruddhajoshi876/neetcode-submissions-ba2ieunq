class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        dir = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        rows, cols = len(grid), len(grid[0])
        queue = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((0,r,c))
        
        while queue:
            n = len(queue)

            for i in range(n):
                cost, r, c = queue.pop(0)

                if (r,c) in visited:
                    continue
                
                visited.add((r,c))
                new_cost = min(grid[r][c], cost+1)
                if grid[r][c] == INF:
                    grid[r][c] = new_cost
                
                for dr, dc in dir:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc] != -1:
                        queue.append((new_cost, nr, nc))
            