class Solution:
    
    def __init__(self):
        self.a_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
    
    def letterCombinations(self, digits):
        if not digits:
            return []
        i = 0
        res = []
        tmp = []
        self.helper(digits, i, tmp, res)
        return res
        
    def helper(self, digits, i, tmp, res):
        if i == len(digits):
            res.append(''.join(tmp))
        else:
            d = digits[i]
            letters = self.a_dict[d]
            for l in letters:
                tmp.append(l)
                self.helper(digits, i+1, tmp, res)
                tmp.pop()
                

if __name__ == '__main__':
    obj = Solution()
    digits = '23'
    print(obj.letterCombinations(digits))
