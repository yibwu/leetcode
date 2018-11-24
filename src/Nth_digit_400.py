class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n

        t = 0
        count = 0
        i = 1
        base = 1
        m = 0
        while t < n:
            t += 9 * i * base
            if t < n:
                m = t
            count += 1
            base *= 10
            i += 1
        res = []
        remain = n - m - 1
        base //= 10

        for k in range(count):
            if k == 0:
                res.append(remain // base // count + 1)
            else:
                res.append(remain // base // count)

            remain %= (base * count)
            base //= 10
        return res[remain]