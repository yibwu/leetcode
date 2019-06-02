class Solution:
    
    def remove_duplicates(self, S):
        stack = []
        for ch in S:
            if not stack:
                stack.append(ch)
            else:
                if stack[-1] == ch:
                    stack.pop(-1)
                else:
                    stack.append(ch)
        return ''.join(stack)


if __name__ == '__main__':
    obj = Solution()
    s = 'abbaca'
    print(obj.remove_duplicates(s))
