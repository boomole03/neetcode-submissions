class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))

        seen = set()
        dis = 1
        while q:
            q_len = len(q)
            for _ in range(q_len):
                r, c = q.popleft()
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    n_r = r + x
                    n_c = c + y

                    if 0 <= n_r < ROWS and 0 <= n_c < COLS and (n_r, n_c) not in seen and grid[n_r][n_c] == 2147483647:
                        grid[n_r][n_c] = dis
                        seen.add((n_r, n_c))
                        q.append((n_r, n_c))
            dis +=1 


