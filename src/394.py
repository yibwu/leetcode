class Solution:
    
    def decodeString(self, s):
        if not s:
            return ''
        if s.isalpha():
            return s
        
        i = 0
        prefix = []
        while i < len(s) and s[i].isalpha():
            prefix.append(s[i])
            i += 1
        j = i
        while j < len(s) and s[j].isnumeric():
            j += 1
        n = 1 if i == j else int(s[i: j])
        
        k = j
        stack = []
        if k < len(s) and s[k] == '[':
            k += 1
            stack.append('[')
        while stack and k < len(s):
            if s[k] == '[':
                stack.append('[')
            elif s[k] == ']':
                stack.pop()
            k += 1
        return ''.join(prefix) + n * self.decodeString(s[j+1: k-1]) + self.decodeString(s[k:])
