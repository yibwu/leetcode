class Solution:
    
    def diStringMatch(self, S):
        res = []
        low, high = 0, len(S)
        
        for ch in S:
            if ch == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        res.append(low)
        return res


if __name__ == '__main__':
    obj = Solution()
    cases = (
        'IDID',
        'III',
        'DDI',
    )

    for c in cases:
        print(obj.diStringMatch(c))
