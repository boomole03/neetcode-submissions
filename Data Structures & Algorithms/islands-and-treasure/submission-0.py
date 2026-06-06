class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        seen = set() 
        queue = deque([])


        for row in range(ROWS):
            for col in range(COLS):
                if not grid[row][col]:
                    queue.append((row,col))
                    seen.add((row, col))



        # bfs to get dis 
        directions = [(-1,0), (1, 0), (0, 1), (0, -1)]
        dis = 1
        while queue: 
            steps = len(queue)

            for _ in range(steps):
                row, col = queue.popleft()

                for x, y in directions:
                    new_row = row + x
                    new_col = col + y

                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in seen and grid[new_row][new_col] != -1:
                        grid[new_row][new_col] = dis
                        queue.append((new_row, new_col))
                        seen.add((new_row, new_col))


            dis +=1 
        