# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k == 0 or len(tinput) < k:
            return []
        heap = self.build_heap(tinput, k)
        for n in tinput[k: ]:
            if heap[0] > n:
                self.adjust_down(heap, n, k)
        heap.sort()
        return heap

    def adjust_down(self, heap, n, k):
        heap[0] = n
        t = 0
        j = 2 * t + 1
        while j < k:
            if j + 1 < k and nums[j] < nums[j + 1]:
                j += 1
            if heap[t] < heap[j]:
                heap[t], heap[j] = heap[j], heap[t]
            t = j
            j = 2 * t + 1

    def build_heap(self, nums, k):
        heap = nums[: k]
        i = (k - 1) // 2

        while i >= 0:
            t = i
            j = 2 * t + 1
            while j < k:
                if j + 1 < k and nums[j] < nums[j + 1]:
                    j += 1
                if nums[t] < nums[j]:
                    heap[t], heap[j] = heap[j], heap[t]
                t = j
                j = 2 * t + 1
            i -= 1
        return heap


if __name__ == '__main__':
    o = Solution()
    nums = [4,5,1,6,2,7,3,8]
    k = 10
    ret = o.GetLeastNumbers_Solution(nums, k)
    print(ret)



