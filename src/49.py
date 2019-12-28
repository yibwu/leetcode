class Solution:

    def groupAnagrams(self, strs):
        a_dict = dict()
        for s in strs:
            ss = ''.join(sorted(list(s)))
            if ss not in a_dict:
                a_dict[ss] = [s]
            else:
                a_dict[ss].append(s)
           
        res = []
        for _, v in a_dict.items():
            res.append(v)
        return res
