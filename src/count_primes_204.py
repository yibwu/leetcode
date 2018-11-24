class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime = False
        not_prime = True
        arr = [is_prime for _ in range(n)]
        for i in range(2, n):
            k = 2
            if arr[i] == is_prime:
                while i * k < n:
                    arr[i * k] = not_prime
                    k += 1
        return arr[2:].count(is_prime)


if __name__ == '__main__':
    o = Solution()
    ret = o.countPrimes(10)
    print(ret)


