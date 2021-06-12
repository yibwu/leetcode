class Solution:
    
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        i = len(T) - 1

        while i >= 0:
            target = T[i]
            while stack and T[stack[-1]] <= target:
                stack.pop()
            res[i] = 0 if not stack else stack[-1] - i
            stack.append(i)
            i -= 1
        return res

