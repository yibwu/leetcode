class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        nums = list(s)
        LEN = len(nums)
        if LEN < k:
            self.swap(nums, 0, LEN - 1)
        elif LEN < 2 * k:
            self.swap(nums, 0, k - 1)
        else:
            count = LEN // 2 // k
            for n in range(count):
                i, j = 2 * k * n, 2 * k * n + k - 1
                self.swap(nums, i, j)
            left = LEN - 2 * count * k
            if left < k:
                self.swap(nums, 2 * count * k, LEN - 1)
            else:
                self.swap(nums, 2 * count * k, 2 * count * k + k - 1)
        return ''.join(nums)

    def swap(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    o = Solution()
    s = "abcdefg"
    k = 2
    ret = o.reverseStr(s, k)
    print(ret)