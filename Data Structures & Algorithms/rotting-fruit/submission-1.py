class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])

        q = deque([])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
        while q and fresh > 0:
            q_len = len(q)
            for _ in range(q_len):
                r, c = q.popleft()
                for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
                    n_r = r + x
                    n_c = c + y

                    if 0 <= n_r < ROWS and 0 <= n_c < COLS and grid[n_r][n_c] == 1:
                        grid[n_r][n_c] = 2
                        fresh -=1 
                        q.append((n_r, n_c))

            res += 1 


        return res if fresh == 0 else -1