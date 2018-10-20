class Solution:
    def sortnumsrrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.helper(nums)
        i, j = 1, len(nums) - 2
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j -= 2


    def helper(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 == 0:
                i += 1
            while i < j and nums[j] % 2 == 1:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1


if __name__ == '__main__':
    o = Solution()
    nums = [3, 1, 2, 4]
    o.sortnumsrrayByParityII(nums)
    print(nums)