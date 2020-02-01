class Solution:
    
    def findDisappearedNumbers(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            while nums[i] != i + 1 and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i] - 1
            i += 1
            
        res = []
        for i, n in enumerate(nums):
            if i + 1 != n:
                res.append(i+1)
        return res
        

if __name__ == '__main__':
    obj = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    res = obj.findDisappearedNumbers(nums)
    print(res)
