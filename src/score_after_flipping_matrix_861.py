class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        row, col = len(A), len(A[0])

        for i in range(row):
            if A[i][0] == 0:
                for j in range(col):
                    A[i][j] = 1 if A[i][j] == 0 else 0

        for j in range(1, col):
            count = 0
            for i in range(row):
                if A[i][j] == 1:
                    count += 1
            if count < row / 2:
                for i in range(row):
                    A[i][j] = 1 if A[i][j] == 0 else 0

        score = 0
        for i in range(row):
            t = 0
            for j in range(col):
                t <<= 1
                t += A[i][j]
            score += t
        return score