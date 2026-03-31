class Solution:
    def pacificAtlantic(self, heights):
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        pac = set()
        atl=set()
        def dfs(r,c, visited):
            visited.add((r,c))

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if 0<=nr<rows and 0<=nc<cols and heights[nr][nc] >= heights[r][c] and (
                    (nr,nc) not in visited):
                    dfs(nr,nc,visited)
        
        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows-1,c, atl)

        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols-1, atl)
        
        res = pac & atl
        return [[r,c] for (r,c) in res]