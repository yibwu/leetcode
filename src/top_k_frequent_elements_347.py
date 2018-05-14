class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_count = {}
        for n in nums:
            num_count[n] = num_count.get(n, 0) + 1

        left = []
        min_heap = []
        count = 0
        for n, cnt in num_count.items():
            if count < k:
                min_heap.append([n, cnt])
                count += 1
            else:
                left.append([n, cnt])
        self.build_heap(min_heap)

        for item in left:
            self.del_from_heap(min_heap, item)
        return [item[0] for item in min_heap]

    def build_heap(self, min_heap):
        i = len(min_heap) // 2 - 1
        while i >= 0:
            self.adjust_down(min_heap, i)
            i -= 1

    def adjust_down(self, min_heap, i):
        while i < len(min_heap):
            j = 2 * i + 1
            k = j + 1
            next_step = j

            if k < len(min_heap) and min_heap[k][1] < min_heap[j][1]:
                next_step = k
            if next_step < len(min_heap) and min_heap[i][1] > min_heap[next_step][1]:
                min_heap[i], min_heap[next_step] = min_heap[next_step], min_heap[i]
                i = next_step
            else:
                break

    def insert_min_heap(self, min_heap, x):
        self.adjust_top(min_heap, x)

    def del_from_heap(self, min_heap, x):
        if min_heap and min_heap[0][1] < x[1]:
            min_heap[0] = x
            self.adjust_down(min_heap, 0)

    def adjust_top(self, min_heap, x):
        i = len(min_heap)
        next_step = i // 2 if i % 2 == 1 else i // 2 - 1

        while i != 0 and next_step >= 0 and x[1] < min_heap[next_step][1]:
            x, min_heap[next_step] = min_heap[next_step], x
            i = next_step
            next_step = i // 2 if i % 2 == 1 else i // 2 - 1


if __name__ == '__main__':
    o = Solution()
    nums = [1, 1, 1, 2, 2, 3, 3, 3]
    k = 2
    top_k = o.topKFrequent(nums, k)
    print(top_k)

