class Solution:
    def count_bits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        for n in range(num + 1):
            count = 0
            while n != 0:
                count += 1
                n &= (n - 1)
            result.append(count)
        return result