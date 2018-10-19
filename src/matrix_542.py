class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        MAX_DISTANCE = 10001

        if not matrix:
            return matrix
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    min_zero_distance = 1
                    for k in range(4):
                        if k == 0:
                            t = j
                            step_right = 1
                            while t+1 < col and matrix[i][t+1] == 1:  # RIGHT
                                t += 1
                                step_right += 1
                            if t+1 == col:
                                step_right = MAX_DISTANCE
                        elif k == 1:
                            t = i
                            step_down = 1
                            while t+1 < row and matrix[t+1][j] == 1:  # DOWN
                                t += 1
                                step_down += 1
                            if t+1 == row:
                                step_down = MAX_DISTANCE
                        elif k == 2:
                            t = j
                            step_left = 1
                            while t-1 >= 0 and matrix[i][t-1] == 1:  # LEFT
                                t -= 1
                                step_left += 1
                            if t-1 == 0:
                                step_left = MAX_DISTANCE
                        elif k == 3:
                            t = i
                            step_up = 1
                            while t-1 >= 0 and matrix[t-1][j] == 1:  # UP
                                t -= 1
                                step_up += 1
                    matrix[i][j] = min([step_right, step_down, step_left, step_up])
        return matrix


if __name__ == '__main__':
    o = Solution()
    matrix = [
        [1, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ]
    ret = o.updateMatrix(matrix)
    print(ret)
