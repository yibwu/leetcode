class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @staticmethod
    def walk_preorder(root):
        if root is not None:
            print(root.val)
            TreeNode.walk_preorder(root.left)
            TreeNode.walk_preorder(root.right)


class Solution:
    def construct_maximum_binarytree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums))

    def helper(self, nums, low, high):
        if low < high:
            val = max(nums[low: high])
            val_idx = nums.index(val)
            root = TreeNode(val)
            root.left = self.helper(nums, low, val_idx)
            root.right = self.helper(nums, val_idx + 1, high)
            return root
        else:
            return None


if __name__ == '__main__':
    o = Solution()
    nums = [3, 2, 1, 6, 0, 5]
    root = o.construct_maximum_binarytree(nums)
    TreeNode.walk_preorder(root)
    
