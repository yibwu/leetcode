class Solution:
    def flip_and_invert_image(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        img = self.reverse_arr(A)
        result = self.flip_arr(img)
        return result

    def reverse_arr(self, arr2d):
        return [arr[::-1] for arr in arr2d]
        
    def flip_arr(self, arr2d):
        return [list(map(lambda x: x ^ 1, arr)) for arr in arr2d]
            

if __name__ == '__main__':
    o = Solution()
    # img = [[1, 1, 0], [1, 0, 1], [0, 0, 0]] 
    img = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    ret = o.flip_and_invert_image(img)
    print(ret)
