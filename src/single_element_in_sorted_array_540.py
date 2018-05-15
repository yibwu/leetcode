class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = None
        if nums:
            result = nums[0]
            for n in nums[1:]:
                result ^= n
        return result


if __name__ == '__main__':
    o = Solution()
    nums = [1, 1, 2, 3, 3]
    ret = o.singleNonDuplicate(nums)
    print(ret)

