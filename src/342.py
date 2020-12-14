class Solution:

    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        
        while n != 1 and n & 3 == 0:
            n >>= 2
        return n == 1

