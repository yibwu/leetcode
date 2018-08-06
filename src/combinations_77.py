class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        index_range = [0, 0]
        self.helper(n, k, result, index_range)
        return result[index_range[0]: index_range[1]]

    def helper(self, n, k, result, index_range):
        if k == 1:
            for i in range(1, n + 1):
                result.append([i])
            index_range[1] = n
        else:
            self.helper(n, k - 1, result, index_range)
            count = 0
            # must add index_range to filter result, otherwise time exceed
            for item in result[index_range[0]: index_range[1]]:
                left = item[-1] + 1
                right = n + 1
                for i in range(left, right):
                    count += 1
                    tmp = item + [i]
                    result.append(tmp)
            index_range[0] = index_range[1]
            index_range[1] += count


if __name__ == '__main__':
    o = Solution()
    n, k = 20, 15
    import time
    start = time.time()
    ret = o.combine(n, k)
    end = time.time()
    print(ret)
    print(end - start)
