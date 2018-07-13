class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper(nums, 0, result)
        return result

    def helper(self, nums, index, result):
        if index == len(nums):
            import copy
            result.append(copy.deepcopy(nums))
        else:
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                self.helper(nums, index + 1, result)
                nums[index], nums[i] = nums[i], nums[index]
        
        
if __name__ == '__main__':
    o = Solution()
    nums = [1, 2, 3]
    ret = o.permute(nums)
    print(ret)
