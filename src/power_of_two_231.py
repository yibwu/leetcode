class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return True if count == 1 else False