class Solution(object):
    
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return grid
        
        a_list = self.matrix_to_list(grid)
        k %= len(a_list)
        self.swap(a_list, 0, len(a_list) - k - 1)
        self.swap(a_list, len(a_list) - k, len(a_list) - 1)
        self.swap(a_list, 0, len(a_list) - 1)        
        
        res = []
        row, col = len(grid), len(grid[0])
        for i in range(row):
            res.append(a_list[col * i: col * i + col])
        return res
        
    def swap(self, a_list, lo, hi):
        while lo < hi:
            a_list[lo], a_list[hi] = a_list[hi], a_list[lo]
            lo += 1
            hi -= 1
    
    def matrix_to_list(self, matrix):
        res = []
        for row in matrix:
            res.extend(row)
        return res
