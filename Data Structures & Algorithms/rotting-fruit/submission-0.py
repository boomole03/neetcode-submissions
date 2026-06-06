class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        m = 0
        
        rotten = deque([])

        for row in range(len(grid)): 
            for col in range(len(grid[0])): 
                if grid[row][col] == 2:
                    rotten.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1

        while rotten and fresh > 0:
            level = len(rotten)
            
            for _ in range(level):
                # check if the near nodes are fresh...
                row, col = rotten.popleft()
                for x, y in [(0,1), (0,-1), (1,0), (-1, 0)]:
                    new_row, new_col = row + x, col + y
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                        rotten.append((new_row, new_col))
                        grid[new_row][new_col] = 2 # we've seen this now
                        fresh -=1 


            m += 1
        print(fresh)


        return m if fresh == 0 else -1