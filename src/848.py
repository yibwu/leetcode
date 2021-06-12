class Solution:

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ss = sum(shifts)
        i = 0
        acc = 0
        while i < len(shifts):
            t = shifts[i]
            shifts[i] = ss - acc
            acc += t
            i += 1
        
        res = list(s)
        i = 0
        while i < len(res):
            res[i] = chr((ord(res[i]) + shifts[i] - ord('a')) % 26 + ord('a'))   
            i += 1
        return ''.join(res)

