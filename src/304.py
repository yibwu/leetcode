class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        matrix.insert(0, [0] * col)
        
        for i in range(1, row+1):
            for j in range(col):
                if j == 0:
                    matrix[i][j] += matrix[i-1][j]
                else:
                    matrix[i][j] += (matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1])

        matrix.pop(0) 
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > row2:
            row1, row2 = row2, row1

        if row1 == 0:
            if col1 == 0:
                return self.matrix[row2][col2]
            else:
                return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        else:
            if col1 == 0:
                return self.matrix[row2][col2] - self.matrix[row1-1][col2]
            else:
                return self.matrix[row2][col2] - self.matrix[row1-1][col2] - self.matrix[row2][col1-1] + self.matrix[row1-1][col1-1]
        
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

