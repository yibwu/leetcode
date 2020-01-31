class Solution:
    
    def __init__(self):
        chars = [chr(ord('A') + i) for i in range(26)]
        self.map = dict()
        for i, c in enumerate(chars):
            self.map[i+1] = c
    
    def convertToTitle(self, n):
        a_list = []
        while n != 0:
            a_list.append(n % 26)
            n = n // 26
        
        i = 0
        carry = False
        while i < len(a_list):
            if carry:
                if a_list[i] == 0:
                    a_list[i] = 25
                elif a_list[i] == 1:
                    if i != len(a_list) - 1:
                        a_list[i] = 26
                    else:
                        a_list[i] = 0
                else:
                    a_list[i] -= 1
                    carry = False
            else:
                if a_list[i] == 0:
                    a_list[i] = 26
                    carry = True
            i += 1
        a_list.reverse()
        
        res = []
        for n in a_list:
            if n != 0:
                res.append(self.map[n])
        return ''.join(res)
