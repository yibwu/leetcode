class Solution:
    def three_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        len_nums = len(nums)
        for i in range(len_nums - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                target = 0 - nums[i]
                low = i + 1
                high = len_nums - 1
                while low < high:
                    if nums[low] + nums[high] == target:
                        result.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < target:
                        low += 1
                    else:
                        high -= 1
        return result


if __name__ == '__main__':
    o = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    result = o.three_sum(nums)
    print(result)