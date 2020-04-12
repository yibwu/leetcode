class Solution:
    
    # 直观版本 
    def intervalIntersection(self, A, B):
        res = []

        for nums1 in A:
            for nums2 in B:
                begin = max(nums1[0], nums2[0])
                end = min(nums1[1], nums2[1])

                if begin <= end:
                    res.append([begin, end])
                    if end == nums1[1]:
                        break
        return res

    # 加速版本
    def intervalIntersection2(self, A, B):
        res = []
        i, j = 0, 0
        
        while i < len(A):
            while j < len(B):
                nums1 = A[i]
                nums2 = B[j]
                if nums1[1] < nums2[0]:
                    break
                begin = max(nums1[0], nums2[0])
                end = min(nums1[1], nums2[1])
                if begin <= end:
                    res.append([begin, end])
                    if end == nums1[1]:
                        break
                j += 1
            i += 1
        return res


if __name__ == '__main__':
    obj = Solution()
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    res = obj.intervalIntersection(A, B)
    print(res)
    res = obj.intervalIntersection2(A, B)
    print(res)
