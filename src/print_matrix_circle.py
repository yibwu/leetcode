# -*- coding:utf-8 -*-

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        row_left = len(matrix)
        col_left = len(matrix[0])
        i, j = 0, 0
        result = []

        while row_left > 0 and col_left > 0:
            for _ in range(col_left):
                result.append(matrix[i][j])
                j += 1
            row_left -= 1
            if row_left == 0:
                break
            i += 1
            j -= 1

            for _ in range(row_left):
                result.append(matrix[i][j])
                i += 1
            col_left -= 1
            if col_left == 0:
                break
            i -= 1
            j -= 1

            for _ in range(col_left):
                result.append(matrix[i][j])
                j -= 1
            row_left -= 1
            if row_left == 0:
                break
            j += 1
            i -= 1

            for _ in range(row_left):
                result.append(matrix[i][j])
                i -= 1
            col_left -= 1
            if col_left == 0:
                break
            i += 1
            j += 1

        return result


if __name__ == '__main__':
    o = Solution()
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # matrix = [[1]]
    # matrix = [[1], [2], [3], [4], [5]]
    ret = o.printMatrix(matrix)
    print(ret)


