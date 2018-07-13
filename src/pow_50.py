class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        negative = True if n < 0 else False
        n = abs(n) if n < 0 else n
        result = self.fast_pow(x, n)
        return 1.0 / result if negative else result
        
    def fast_pow(self, base, n):
        if n == 0:
            return 1
        elif n % 2 == 0:
            t = self.fast_pow(base, n // 2)
            return t * t
        else:
            return base * self.fast_pow(base, n - 1)


if __name__ == '__main__':
    o = Solution()
    base, n = 2.00000, 10
    base, n = 2.10000, 3
    base, n = 2.00000, -2
    ret = o.myPow(base, n)
    print(ret)
