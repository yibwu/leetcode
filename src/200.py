class Solution:
    
    def __init__(self):
        self.visited = set()
        
    def gen_key(self, x, y):
        return str(x) + '_' + str(y)
        
    def mark_visited(self, x, y):
        self.visited.add(self.gen_key(x, y))
        
    def has_visited(self, x, y):
        return self.gen_key(x, y) in self.visited
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and not self.has_visited(i, j):
                    res += 1
                    self.dfs(grid, i, j, row, col)
        return res
    
    def dfs(self, grid, i, j, row, col):
        self.mark_visited(i, j)
        if j+1 < col and grid[i][j+1] == '1' and not self.has_visited(i, j+1):
            self.dfs(grid, i, j+1, row, col)
        if i+1 < row and grid[i+1][j] == '1' and not self.has_visited(i+1, j):
            self.dfs(grid, i+1, j, row, col)
        if j-1 >= 0 and grid[i][j-1] == '1' and not self.has_visited(i, j-1):
            self.dfs(grid, i, j-1, row, col)
        if i-1 >= 0 and grid[i-1][j] == '1' and not self.has_visited(i-1, j):
            self.dfs(grid, i-1, j, row, col)
