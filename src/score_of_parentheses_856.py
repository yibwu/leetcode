class Solution(object):
    def score_of_parentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        return self.helper(S)

    def helper(self, s):
        index = self.find_right_index(s)
        if index == len(s):
            if len(s) == 2:
                return 1
            else:
                return 2 * self.helper(s[1: -1])
        else:
            a = self.helper(s[: index])
            b = self.helper(s[index:])
            return a + b

    def find_right_index(self, s):
        i, j = 0, 1
        stack = [s[0]]
        while stack and j < len(s):
            if s[j] == '(':
                stack.append('(')
            else:
                stack.pop()
            j += 1
        return j


if __name__ == '__main__':
    o = Solution()
    s = "()"
    s = "()()"
    s = "(())"
    s = "(()(()))"
    ret = o.score_of_parentheses(s)
    print(ret)