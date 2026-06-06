class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == '1':
                grid[r][c] = "#"

                dfs(r - 1, c)
                dfs(r + 1, c)
                dfs(r, c - 1)
                dfs(r, c + 1)
                

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1': 
                    dfs(row, col)
                    res +=1
    
        return res