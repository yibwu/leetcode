class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        unduplicate_set = set()
        tmp_arr = []
        self.helper(candidates, target, result, unduplicate_set, tmp_arr)
        return result

    def check_duplicate(self, unduplicate_set, array):
        arr = sorted(array)
        arr = list(map(lambda x: str(x), arr))
        s = ','.join(arr)
        if s not in unduplicate_set:
            unduplicate_set.add(s)
            return False
        else:
            return True

    def helper(self, candidates, target, result, unduplicate_set, tmp_arr):
        if target < 0:
            return
        elif target == 0:
            is_dup = self.check_duplicate(unduplicate_set, tmp_arr)
            if not is_dup:
                import copy
                result.append(copy.deepcopy(tmp_arr))
            return
        else:
            for i in range(len(candidates)):
                tmp_arr.append(candidates[i])
                self.helper(candidates, target - candidates[i], result, unduplicate_set, tmp_arr)
                tmp_arr.pop()


if __name__ == '__main__':
    o = Solution()
    candidates = [2, 3, 5]
    target = 7
    ret = o.combinationSum(candidates, target)
    print(ret)