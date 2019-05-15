class Solution:

    def removeOuterParentheses(self, S):
        stack = []
        result = []
        
        for ch in S:
            if ch == '(':
                stack.append(ch)
                if len(stack) > 1:
                    result.append(ch)
            else:
                if len(stack) > 1:
                    result.append(ch)
                if stack:
                    stack.pop(-1)
        return ''.join(result)


if __name__ == '__main__':
    obj = Solution()
    cases = (
        '(()())(())',
        '(()())(())(()(()))',
        '()()',
        '((()))()',
    )
    for s in cases:
        print(obj.removeOuterParentheses(s))
