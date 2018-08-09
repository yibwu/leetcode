class Solution:
    def can_jump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = len(nums) - 2
        start = i + 1
        while i >= 0:
            if start - i <= nums[i]:
                start = i
                i = start - 1
            else:
                i -= 1
        return True if i + 1 == start else False


if __name__ == '__main__':
    o = Solution()
    nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 1, 0, 4]
    ret = o.can_jump(nums)
    print(ret)
