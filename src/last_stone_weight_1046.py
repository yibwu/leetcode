class Solution:

    def last_stone_weight(self, stones):
        self.build_heap(stones)
        while len(stones) > 1:
            a, b = self.get_max_two_element(stones)
            if a == b:
                x = stones.pop(-1)
                y = stones.pop(-1)
                if len(stones) == 0:
                    return 0
                elif len(stones) == 1:
                    return x
                else:
                    stones[0] = x
                    stones[1] = y
                    self.adjust_heap(stones, 1)
                    self.adjust_heap(stones, 0)
            else:
                diff = a - b
                x = stones.pop(-1)
                if len(stones) == 1:
                    return diff 
                elif len(stones) == 2:
                    stones[0] = x
                    stones[1] = diff 
                    self.adjust_heap(stones, 0)
                else:
                    stones[0] = x
                    stones[1] = diff 
                    self.adjust_heap(stones, 1)
                    self.adjust_heap(stones, 0)
        return stones[0]

    def get_max_two_element(self, nums):
        if len(nums) == 2:
            return nums[0], nums[1]
        else:
            if nums[1] > nums[2]:
                return nums[0], nums[1] 
            else:
                nums[1], nums[2] = nums[2], nums[1]
                self.adjust_heap(nums, 2)
                return nums[0], nums[1]

    def adjust_heap(self, nums, index):
        j = index 
        k = 2 * j + 1
        while j < len(nums) and k < len(nums):
            if k + 1 < len(nums) and nums[k] < nums[k + 1]:
                k += 1
            if nums[j] < nums[k]:
                nums[j], nums[k] = nums[k], nums[j]
                j = k
                k = 2 * j + 1
            else:
                break

    def build_heap(self, nums):
        i = len(nums) // 2 - 1
        while i >= 0:
            self.adjust_heap(nums, i)
            i -= 1

 
if __name__ == '__main__':
    obj = Solution()
    cases = [
        [1, 1, 1, 1], 
        [1, 2, 3, 4, 5, 6],
        [2, 7, 4, 1, 8, 1],
        [857, 149, 920, 468, 623, 117, 984, 537, 51, 160, 512, 271, 852, 372, 728, 160, 512, 363, 292, 838, 802, 459, 961, 837, 165, 203, 133, 518, 184, 733],
    ]
    for nums in cases:
        res = obj.last_stone_weight(nums)
        print(res)
