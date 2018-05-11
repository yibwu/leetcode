class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        visited = set()
        connected_component = []
        target = "O"
        
        i = 0
        while i < len(board):
            j = 0
            while j < len(board[i]):
                if board[i][j] == target and self.position(i, j) not in visited:
                    self.helper(board, i, j, visited, connected_component, target)
                    self.check_surrounded(connected_component, board)
                    connected_component = []
                j += 1
            i += 1
        return board

    def position(self, i, j):
        return str(i) + ',' + str(j)

    def check_column(self, x, y, board):
        if x == 0 or x == len(board) - 1:
            return False
        else:
            flag = False
            for i in range(x):
                if board[i][y] == 'X':
                    flag = True
                    break
            for i in range(x + 1, len(board)):
                if board[i][y] == 'X':
                    flag &= True
                    break
            return flag

    def check_row(self, x, y, board):
        if y == 0 or y == len(board[0]) - 1:
            return False
        else:
            flag = False
            for j in range(y):
                if board[x][j] == 'X':
                    flag = True
                    break
            for j in range(y + 1, len(board[0])):
                if board[x][j] == 'X':
                    flag &= True
                    break
            return flag

    def check_postion(self, x, y, board):
        return True if self.check_row(x, y, board) and self.check_column(x, y, board) else False

    def check_surrounded(self, connected_component, board):
        flag = True
        for pos in connected_component:
            x = pos[0]
            y = pos[1]
            if not self.check_postion(x, y, board):
                flag = False
                break
            else:
                pass
        if flag:
            for pos in connected_component:
                x = pos[0]
                y = pos[1]
                board[x][y] = "X"

    def helper(self, board, i, j, visited, connected_component, target):
        visited.add(self.position(i, j))
        connected_component.append((i, j))
        
        for direction in range(0, 4):
            if direction == 0:
                if i - 1 >= 0 and board[i - 1][j] == target and self.position(i - 1, j) not in visited:
                    self.helper(board, i - 1, j, visited, connected_component, target)
            elif direction == 1:
                if j + 1 < len(board[0]) and board[i][j + 1] == target and self.position(i, j + 1) not in visited:
                    self.helper(board, i, j + 1, visited, connected_component, target)
            elif direction == 2:
                if i + 1 < len(board) and board[i + 1][j] == target and self.position(i + 1, j) not in visited:
                    self.helper(board, i + 1, j, visited, connected_component, target)
            else:
                if j - 1 >= 0 and board[i][j - 1] == target and self.position(i, j - 1) not in visited:
                    self.helper(board, i, j - 1, visited, connected_component, target)


if __name__ == '__main__':
    o = Solution()
    # board = [
    #     ["X", "X", "X", "X"],
    #     ["X", "O", "O", "X"],
    #     ["X", "X", "O", "X"],
    #     ["X", "O", "X", "X"]]
    board = [
        ["O", "X", "X", "O", "X"],
        ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"]]
    ret = o.solve(board)
    print(ret)

