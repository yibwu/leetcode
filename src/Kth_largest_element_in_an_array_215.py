class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = self.quick_sort(nums, k, 0, len(nums) - 1)
        return ret

    def quick_sort(self, nums, k, left, right):
        if left < right:
            pivot = self.partition(nums, left, right)
            print(pivot, nums)
            if pivot == k - 1:
                return nums[pivot]
            elif pivot < k - 1:
                return self.quick_sort(nums, k, pivot, right)
            else:
                return self.quick_sort(nums, k, left, pivot)
        else:
            print('--')
            return nums[right]

    def partition(self, nums, left, right):
        tmp = nums[right]
        print(tmp, left, right, nums)
        while left < right:
            while left < right and nums[left] > tmp:
                left += 1
            while left < right and nums[right] < tmp:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return right


if __name__ == '__main__':
    o = Solution()
               # 1     4
               # p     k
    # nums = [3,2,1,5,6,4]
    # k = 2
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    ret = o.findKthLargest(nums, k)
    print(nums)
    print(ret)