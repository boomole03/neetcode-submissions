class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        we need to store what we have seen in each row, col and 3x3 box

        0    1   2
        xxx xxx xxx 0
        xxx xxx xxx 1
        xxx xxx xxx 2
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]


        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue

                if val in rows[row]:
                    return False
                if val in cols[col]:
                    return False
                box_idx = (row//3) * 3 + (col // 3)
                # 
                if val in boxes[box_idx]:
                    return False

                rows[row].add(val)
                cols[col].add(val)
                boxes[box_idx].add(val)


        return True