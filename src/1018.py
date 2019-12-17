class Solution:
    
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        acc = 0
        for n in A:
            acc = acc * 2 + n
            if acc % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
