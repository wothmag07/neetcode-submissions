class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        maxarea = 0
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            grid[r][c] = 0
            area = 1
            for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    area += dfs(nr, nc)
            return area
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    maxarea = max(maxarea, dfs(r, c))
        return maxarea
                    

        