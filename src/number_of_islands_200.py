class Solution:
    def num_islands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        nums = 0

        i = 0
        while i < len(grid):
            j = 0
            while j < len(grid[i]):
                if grid[i][j] == "1" and self.position(i, j) not in visited:
                    self.helper(grid, i, j, visited)
                    nums += 1
                j += 1
            i += 1
        return nums

    def position(self, i, j):
        return str(i) + ',' + str(j)

    def helper(self, grid, i, j, visited):
        visited.add(self.position(i, j))

        for direction in range(0, 4):
            if direction == 0:
                if i - 1 >= 0 and grid[i - 1][j] == "1" and self.position(i - 1, j) not in visited:
                    self.helper(grid, i - 1, j, visited)
            elif direction == 1:
                if j + 1 < len(grid[0]) and grid[i][j + 1] == "1" and self.position(i, j + 1) not in visited:
                    self.helper(grid, i, j + 1, visited)
            elif direction == 2:
                if i + 1 < len(grid) and grid[i + 1][j] == "1" and self.position(i + 1, j) not in visited:
                    self.helper(grid, i + 1, j, visited)
            else:
                if j - 1 >= 0 and grid[i][j - 1] == "1" and self.position(i, j - 1) not in visited:
                    self.helper(grid, i, j - 1, visited)


if __name__ == '__main__':
    o = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    ret = o.num_islands(grid)
    print(ret)

