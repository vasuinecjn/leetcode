class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    r = f"{num} in row {i}"
                    c = f"{num} in column {j}"
                    bx = f"{num} in box {int(i/3)},{int(j/3)}"
                    if r in seen or c in seen or bx in seen:
                        return False
                    else:
                        seen.add(r)
                        seen.add(c)
                        seen.add(bx)
        return True



print(Solution().isValidSudoku(
    [
        [".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],

        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],

        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]
    ]))