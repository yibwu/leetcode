class Solution:
    
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ROW = len(board)
        COL = len(board[0])
        
        rook_x, rook_y = 0, 0
        found = False  
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'R':
                    rook_x, rook_y = i, j
                    found = True
                    break
            if found:
                break
        
        cnt = 0
        
        # north
        x, y = rook_x - 1, rook_y
        while x >= 0:
            if board[x][y] == '.':
                x -= 1
            elif board[x][y] == 'B':
                break
            elif board[x][y] == 'p':
                cnt += 1
                break
                
        # east
        x, y = rook_x, rook_y + 1
        while y < COL:
            if board[x][y] == '.':
                y += 1
            elif board[x][y] == 'B':
                break
            elif board[x][y] == 'p':
                cnt += 1
                break
        
        # south
        x, y = rook_x + 1, rook_y
        while x < ROW:
            if board[x][y] == '.':
                x += 1
            elif board[x][y] == 'B':
                break
            elif board[x][y] == 'p':
                cnt += 1
                break
        
        # west
        x, y = rook_x, rook_y - 1
        while y >= 0:
            if board[x][y] == '.':
                y -= 1
            elif board[x][y] == 'B':
                break
            elif board[x][y] == 'p':
                cnt += 1
                break
                
        return cnt
