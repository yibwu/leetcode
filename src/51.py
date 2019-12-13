class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Solution:
    
    def solveNQueens(self, n):
        queensList = []
        tmp = []
        self.helper(tmp, queensList, 0, n)

        res = []
        for queens in queensList:
            matrix = [['.' for _ in range(n)] for _ in range(n)]
            self.placeQueens(matrix, queens)
            aList = list(map(lambda x: ''.join(x), matrix))
            res.append(aList)
        return res

    def placeQueens(self, matrix, points):
        for p in points:
            matrix[p.x][p.y] = 'Q'
        
    def isValid(self, points, point):
        for p in points:
            if p.x == point.x or p.y == point.y or abs(p.x - point.x) == abs(p.y - point.y):
                return False
        return True
        
    def helper(self, tmp, res, row, n):
        if len(tmp) == n:
            res.append(tmp + [])
        else:
            for col in range(n):
                p = Point(row, col)
                if self.isValid(tmp, p):
                    tmp.append(p)
                    self.helper(tmp, res, row+1, n)
                    tmp.pop()


if __name__ == '__main__':
    obj = Solution()
    cases = [i for i in range(1, 5)]
    for c in cases:
        print(obj.solveNQueens(c))
