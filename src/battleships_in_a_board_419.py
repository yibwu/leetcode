class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rows = len(board)
        cols = len(board[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'X':
                    if i == 0:
                        if j == 0 or board[i][j - 1] == '.':
                            count += 1
                    else:
                        if j == 0 and board[i - 1][j] == '.':
                                count += 1
                        elif board[i - 1][j] == '.' and board[i][j - 1] == '.':
                                count += 1
                else:
                    pass
        return count


if __name__ == '__main__':
    o = Solution()
    board = [['.', '.'], ['X', 'X']]
    ret = o.countBattleships(board)
    print(ret)
