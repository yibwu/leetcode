class Solution:
    def max_area_of_island(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        max_area = 0

        i = 0
        while i < len(grid):
            j = 0
            while j < len(grid[i]):
                if grid[i][j] == 1 and self.position(i, j) not in visited:
                    arr = [0]
                    self.helper(grid, i, j, visited, arr)
                    if max_area < arr[0]:
                        max_area = arr[0]
                j += 1
            i += 1
        return max_area

    def position(self, i, j):
        return str(i) + ',' + str(j)

    def helper(self, grid, i, j, visited, arr):
        arr[0] += 1
        visited.add(str(i) + ',' + str(j))

        for direction in range(0, 4):
            if direction == 0 and i - 1 >= 0 and grid[i - 1][j] == 1 and self.position(i - 1, j) not in visited:
                    self.helper(grid, i - 1, j, visited, arr)
            elif direction == 1 and j + 1 < len(grid[0]) and grid[i][j + 1] == 1 and self.position(i, j + 1) not in visited:
                    self.helper(grid, i, j + 1, visited, arr)
            elif direction == 2 and i + 1 < len(grid) and grid[i + 1][j] == 1 and self.position(i + 1, j) not in visited:
                    self.helper(grid, i + 1, j, visited, arr)
            elif j - 1 >= 0 and grid[i][j - 1] == 1 and self.position(i, j - 1) not in visited:
                    self.helper(grid, i, j - 1, visited, arr)
            else:
                pass


if __name__ == '__main__':
    o = Solution()
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    ret = o.max_area_of_island(grid)
    print(ret)

