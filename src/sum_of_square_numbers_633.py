class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        limit = int(math.sqrt(c))
        if limit * limit == c:
            return limit, limit, True

        for i in range(0, limit + 1):
            j = limit
            while j >= 0:
                if i * i + j * j == c:
                    return i, j, True
                j -= 1
        return 0, 0, False


if __name__ == '__main__':
    o = Solution()
    for i in range(1000000000, 1000000001):
        a, b, ret = o.judgeSquareSum(i)
        print(i, a, b, ret)