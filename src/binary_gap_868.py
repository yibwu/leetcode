class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)[2:]
        has_occurs = False
        i, lens = 0, len(s)
        last_visited = 0
        max_distance = 0

        while i < lens:
            if s[i] == '1':
                if has_occurs:
                    max_distance = max_distance if i - last_visited < max_distance else i - last_visited
                    last_visited = i
                else:
                    last_visited = i
                    has_occurs = True
            i += 1
        return max_distance


if __name__ == '__main__':
    o = Solution()
    n = 9
    ret = o.binaryGap(n)
    print(ret)