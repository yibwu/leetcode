class Solution:

    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        a_dict1 = dict()
        a_dict2 = dict()
        i = 0
        
        while i < len(s):
            c1, c2 = s[i], t[i]
            
            if c1 not in a_dict1 and c2 not in a_dict2:
                a_dict1[c1] = c2
                a_dict2[c2] = c1
            elif c1 in a_dict1 and c2 not in a_dict2:
                return False
            elif c2 in a_dict2 and c1 not in a_dict1:
                return False
            elif c1 in a_dict1 and c2 != a_dict1[c1]:
                return False
            elif c2 in a_dict2 and c1 != a_dict2[c2]:
                return False
            i += 1
        return True
