class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        res = 0 
        row, col = len(grid), len(grid[0])

        def dfs(x, y):
            if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                grid[x][y] = 0 
                return 1 + dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1)
            return 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1: 
                    # do the dfs
                    l = dfs(r, c)
                    res = max(l, res)

        return res