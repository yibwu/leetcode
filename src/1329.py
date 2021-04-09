class Solution:
    
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        x, y = 0, col - 1
        
        while x < row and y >= 0:
            i, j = x, y
            arr = []
            while i < row and j < col:
                arr.append(mat[i][j])
                i += 1
                j += 1
                
            arr.sort()
            i, j = x, y
            while i < row and j < col:
                mat[i][j] = arr.pop(0)
                i += 1
                j += 1
                
            y -= 1
            if y < 0:
                x += 1
                y = 0
        return mat

