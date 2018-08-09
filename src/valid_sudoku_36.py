class Solution:
    def is_valid_sudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.check_row(board) and \
               self.check_column(board) and \
               self.check_sub_box(board)

    def check_row(self, board):
        nums = set()
        for row in board:
            for val in row:
                if val != '.':
                    if val not in nums:
                        nums.add(val)
                    else:
                        return False
                else:
                    pass
            nums = set()
        return True

    def check_column(self, board):
        nums = set()
        for col in range(9):
            for row in range(9):
                val = board[row][col]
                if val != '.':
                    if val not in nums:
                        nums.add(val)
                    else:
                        return False
                else:
                    pass
            nums = set()
        return True

    def check_sub_box(self, board):
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                nums = set()
                for i in range(0, 3):
                    for j in range(0, 3):
                        val = board[row + i][col + j]
                        if val != '.':
                            if val not in nums:
                                nums.add(val)
                            else:
                                return False
                        else:
                            pass
        return True


if __name__ == '__main__':
    o = Solution()
    board = \
    [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    # board = \
    # [
    #     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    # ]
    ret = o.is_valid_sudoku(board)
    print(ret)

