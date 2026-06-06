class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i, seen):
            if (0 <=  r < ROWS and 0 <= c < COLS and i < len(word) and board[r][c] == word[i] and (r, c) not in seen):
                i += 1
                if i == len(word):
                    return True

                seen.add((r,c))
                lol = dfs(r-1, c, i, seen) or dfs(r+1, c, i, seen) or dfs(r, c-1, i, seen) or dfs(r, c+1, i, seen)
                seen.remove((r,c))
                return lol

            return False

        for row in range(ROWS):
            for col in range(COLS):
                visited = set()
                if dfs(row, col, 0, visited):
                    res = True
                    break

        return res