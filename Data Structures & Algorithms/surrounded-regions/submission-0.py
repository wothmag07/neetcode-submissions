class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return []

        m, n = len(board), len(board[0])
        visited = set()

        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        def bfs():
            q = deque()
            for r in range(m):
                for c in range(n):
                    if (r == 0 or r == m-1 or c == 0 or c == n-1) and board[r][c] == 'O':
                        q.append((r,c))
                        board[r][c] = 'T'
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                        board[nr][nc] = "T"
                        q.append((nr, nc))
        
        bfs()

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"
        