class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        visited = set()

        def dfs(r, c):
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1" and (nr,nc) not in visited:
                    dfs(nr, nc)
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i, j)
                    islands += 1
        return islands
        