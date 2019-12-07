class Solution(object):

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n > (19-k) * k // 2:
            return []
        
        res = []
        acc = []
        hi = n if n < 10 else 9
        self.helper(k, n, 1, hi + 1, res, acc)
        return res
    
    def helper(self, k, target, lo, hi, res, acc):
        for n in range(lo, hi):
            if k == 1 and sum(acc) + n == target:
                res.append(acc + [n])
                break
            elif sum(acc) + n < target:
                self.helper(k - 1, target, n + 1, hi, res, acc + [n])
            else:
                break
