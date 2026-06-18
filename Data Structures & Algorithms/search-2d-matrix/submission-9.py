class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l = 0
        r = ROWS * COLS - 1 

        while l <= r:
            m = ((r - l) // 2 + l)
            row = m // COLS
            col = m % COLS
            print("m: ", m, ' row: ', row, ' col:', col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1

        return False