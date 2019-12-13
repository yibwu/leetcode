class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Solution:
    
    def totalNQueens(self, n):
        res = [0]
        tmp = []
        self.helper(tmp, res, 0, n)
        return res[0]
        
    def isValid(self, points, point):
        for p in points:
            if p.x == point.x or p.y == point.y or abs(p.x - point.x) == abs(p.y - point.y):
                return False
        return True
        
    def helper(self, tmp, res, row, n):
        if len(tmp) == n:
            res[0] += 1
        else:
            for col in range(n):
                p = Point(row, col)
                if self.isValid(tmp, p):
                    tmp.append(p)
                    self.helper(tmp, res, row+1, n)
                    tmp.pop()


if __name__ == '__main__':
    obj = Solution()
    cases = [i for i in range(1, 10)]
    for c in cases:
        print(c, obj.totalNQueens(c))
