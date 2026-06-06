class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if (0 <=  r < ROWS and 0 <= c < COLS and i < len(word) and board[r][c] == word[i]):
                i += 1
                if i == len(word):
                    return True

                tmp = board[r][c]
                board[r][c] = "#"
                lol = dfs(r-1, c, i) or dfs(r+1, c, i) or dfs(r, c-1, i) or dfs(r, c+1, i)
                board[r][c] = tmp
                return lol

            return False

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True

        return res