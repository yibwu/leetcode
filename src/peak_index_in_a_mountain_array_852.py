class Solution:
    def peak_index_in_mountain_array(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        end = len(A) - 1
        i = 1
        while i < end and A[i] > A[i - 1] and A[i] < A[i + 1]:
            i += 1
        return i
