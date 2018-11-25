class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        view_from_top = []
        view_from_left = []

        for j in range(col):
            tmp = 0
            for i in range(row):
                tmp = grid[i][j] if grid[i][j] > tmp else tmp
            view_from_top.append(tmp)

        for i in range(row):
            tmp = 0
            for j in range(col):
                tmp = grid[i][j] if grid[i][j] > tmp else tmp
            view_from_left.append(tmp)

        acc = 0
        for i in range(row):
            for j in range(col):
                target = min(view_from_left[i], view_from_top[j])
                acc += (target - grid[i][j])
        return acc