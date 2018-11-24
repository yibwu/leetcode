class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [False for _ in range(n)]
        for i in range(2, n):
            k = 2
            if not arr[i]:
                while i * k < n:
                    arr[i * k] = True
                    k += 1
        return arr[2:].count(False)


if __name__ == '__main__':
    o = Solution()
    o.countPrimes(10)


