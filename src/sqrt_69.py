class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 1, x

        while left <= right:
            mid = left + (right - left) // 2
            if mid < x / mid:
                left = mid + 1
            elif mid > x / mid:
                right = mid - 1
            else:
                right = mid
                break
        return right


if __name__ == '__main__':
    o = Solution()
    for i in range(1, 101):
        ret = o.mySqrt(i)
        print(i, ret)
