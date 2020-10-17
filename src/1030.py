class Solution:
    
    def distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        arr = []
        for i in range(R):
            for j in range(C):
                arr.append([[i, j], self.distance(i, j, r0, c0)])
        
        arr.sort(key=lambda x: x[1])
        return list(map(lambda x: x[0], arr))
