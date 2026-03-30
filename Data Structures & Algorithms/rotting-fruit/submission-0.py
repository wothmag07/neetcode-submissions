class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        """
        grid = [[1,1,0],
                [0,1,1],
                [0,1,2]]
        """
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        time = 0

        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        directions = [(-1,0),(0,1),(1,0),(0,-1)]

    
        while fresh > 0 and queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1




        
        