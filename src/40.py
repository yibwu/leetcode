class Solution:

    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        tmp = []
        a_set = set()
        self.helper(candidates, tmp, res, 0, target, a_set)
        return res
    
    def key(self, nums):
        nums = list(map(lambda x: str(x), nums))
        return '_'.join(nums)
    
    def helper(self, nums, tmp, res, i, target, a_set):
        if target < 0:
            return
        elif target == 0:
            k = self.key(tmp)
            if k not in a_set:
                a_set.add(k)
                res.append(tmp + [])
        else:
            for j, n in enumerate(nums[i:]):
                if target >= n:
                    tmp.append(n)
                    self.helper(nums, tmp, res, i+j+1, target-n, a_set)
                    tmp.pop()
