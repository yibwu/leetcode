class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LEN = len(nums)
        left_sum = 0
        right_sum = sum(nums)

        pivot = -1
        for i in range(0, LEN):
            right_sum -= nums[i]
            if left_sum == right_sum:
                pivot = i
                break
            else:
                left_sum += nums[i]
        return pivot


if __name__ == '__main__':
    o = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    # nums = [1, 2, 3]
    # nums = [-1, -1, -1, -1, -1, -1]
    ret = o.pivotIndex(nums)
    print(ret)


