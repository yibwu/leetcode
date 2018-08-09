class Solution(object):
    def max_sub_array(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = 0
        tmp_sum = 0

        for n in nums:
            tmp_sum += n
            if tmp_sum > 0:
                max_val = tmp_sum if tmp_sum > max_val else max_val
            else:
                tmp_sum = 0
        return max_val if max(nums) > 0 else max(nums)


if __name__ == '__main__':
    o = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [-1]
    ret = o.max_sub_array(nums)
    print(ret)
