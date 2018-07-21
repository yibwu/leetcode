class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        row = len(A)
        col = len(A[0])
        
        for i in range(col):
            t = [A[j][i] for j in range(row)]
            result.append(t)
        return result
