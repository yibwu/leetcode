class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        
class Solution:
    
    def isBoomerang(self, points):
        points.sort()
        p0, p1, p2 = (Point(p[0], p[1]) for p in points)
        
        if p0.x == p1.x == p2.x or p0.y == p1.y == p2.y:
            return False
        
        tan = (p2.y - p0.y) / (p2.x - p0.x) 
        return False if tan * (p1.x - p0.x) + p0.y == p1.y else True


if __name__ == '__main__':
    cases = [
        [[1, 1], [2, 3], [3, 2]],
        [[1, 1], [2, 2], [3, 3]],
    ]
    obj = Solution()
    for c in cases:
        res = obj.isBoomerang(c)
        print(res)
