class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        i, j = 0, 0
        stack = []

        while i != len(pushed) and j != len(popped):
            if pushed[i] != popped[j]:
                stack.append(pushed[i])
                i += 1
            else:
                i += 1
                j += 1
                if stack:
                    while stack and stack[-1] == popped[j]:
                        stack.pop()
                        j += 1

        return False if stack else True