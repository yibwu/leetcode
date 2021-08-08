class TreeNode:
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = self.buildSegmentTree(nums, 0, len(nums)-1)
        
    def buildSegmentTree(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])
        
        mid = start + (end - start) // 2
        root = TreeNode(0)
        root.left = self.buildSegmentTree(nums, start, mid)
        root.right = self.buildSegmentTree(nums, mid+1, end)
        if root.left and root.right:
            root.val = root.left.val + root.right.val
        if root.left and not root.right:
            root.val = root.left.val
        if not root.left and root.right:
            root.val = root.right.val
        return root
        
    def update(self, index: int, val: int) -> None:
        self.updateHelper(index, val, 0, len(self.nums)-1, self.root)
        self.nums[index] = val
        
    def updateHelper(self, index, val, start, end, root):     
        if start > end:
            return
        if start == end:
            root.val += (val - self.nums[index])
            return
        
        mid = start + (end - start) // 2
        if index <= mid:
            self.updateHelper(index, val, start, mid, root.left)
        else:
            self.updateHelper(index, val, mid+1, end, root.right)
        root.val += (val - self.nums[index])

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeHelper(left, right, 0, len(self.nums)-1, self.root)

    def sumRangeHelper(self, left, right, start, end, root):
        if right < start or left > end:
            return 0
        if left <= start and right >= end:
            return root.val
        
        mid = start + (end - start) // 2
        sumLeft = self.sumRangeHelper(left, right, start, mid, root.left)
        sumRight = self.sumRangeHelper(left, right, mid+1, end, root.right)
        return sumLeft + sumRight
    
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

