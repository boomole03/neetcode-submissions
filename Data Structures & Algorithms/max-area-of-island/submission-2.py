class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        m = {}
        i = 0

        def dfs(r, c, i):
            nonlocal m
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c]:
                grid[r][c] = 0
                m[i] += 1

                dfs(r + 1, c, i)
                dfs(r - 1, c, i)
                dfs(r, c - 1, i)
                dfs(r, c + 1, i)
                return
    
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1: 
                    m[i] = 0
                    dfs(row, col, i)
                    max_area = max(max_area, m[i])
                    i += 1

        return max_area 