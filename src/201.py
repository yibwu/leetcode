class Solution:
    
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == n:
            return m

        bits_m = bin(m)[2:]
        bits_n = bin(n)[2:]
        if len(bits_m) != len(bits_n):
            return 0
        else:
            t = 1 << (len(bits_m) - 1)
            return t + self.rangeBitwiseAnd(m - t, n - t)
