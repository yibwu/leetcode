class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A) - 1
        while i < j:
            while i < j and A[i] % 2 == 0:
                i += 1
            while i < j and A[j] % 2 == 1:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1


if __name__ == '__main__':
    o = Solution()
    nums = [1, 2, 4, 3]
    o.sortArrayByParity(nums)
    print(nums)