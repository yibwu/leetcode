class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = set()
        self.helper(n, result)
        res = list(filter(lambda x: len(x) == 2 * n, result))
        return res

    def helper(self, n, result):
        if n == 1:
            result.add('()')
            return
        else:
            self.helper(n - 1, result)
            res = list(filter(lambda x: len(x) == 2 * (n - 1), result))
            for s in res:
                for i in range(len(s) + 1):
                    new_pair = s[:i] + '()' + s[i:]
                    result.add(new_pair)
            return


if __name__ == '__main__':
    o = Solution()
    n = 3
    ret = o.generateParenthesis(n)
    print(ret)