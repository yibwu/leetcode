class Solution(object):
    
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        visited = set()
        self.dfs(sr, sc, visited, image, image[sr][sc], newColor)
        return image
        
    def key(self, i, j):
        return str(i) + '_' + str(j)
        
    def dfs(self, i, j, visited, image, old_color, new_color):
        visited.add(self.key(i, j))
        image[i][j] = new_color
        
        for k in range(4):
            if k == 0:  # right
                if j + 1 < len(image[0]) and image[i][j+1] == old_color and self.key(i, j + 1) not in visited:
                    self.dfs(i, j + 1, visited, image, old_color, new_color)
            elif k == 1: # down
                if i + 1 < len(image) and image[i+1][j] == old_color and self.key(i + 1, j) not in visited:
                    self.dfs(i + 1, j, visited, image, old_color, new_color)
            elif k == 2: # left
                if j - 1 >= 0 and image[i][j-1] == old_color and self.key(i, j - 1) not in visited:
                    self.dfs(i, j - 1, visited, image, old_color, new_color)
            else: # up
                if i - 1 >= 0 and image[i-1][j] == old_color and self.key(i - 1, j) not in visited:
                    self.dfs(i - 1, j, visited, image, old_color, new_color)
