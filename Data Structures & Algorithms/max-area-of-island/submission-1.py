class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS, res = len(grid), len(grid[0]), 0

        def dfs(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1:
                grid[r][c] = 0
                return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            return 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    res = max(res, area)

        return res