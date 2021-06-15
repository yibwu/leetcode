class Solution:
    
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = []
        for _ in range(row + 2):
            dp.append([0 for _ in range(col + 2)])
        
        res = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    res += dp[i+1][j+1]
                else:
                    dp[i+1][j+1] = 0
        return res

