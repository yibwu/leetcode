class Solution:
    
    def minSetSize(self, arr: List[int]) -> int:
        a_dict = dict()
        for n in arr:
            a_dict[n] = a_dict.get(n, 0) + 1
        a_list = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)
        
        res = 0
        cnt = 0
        for item in a_list:
            cnt += item[1]
            res += 1
            if cnt >= len(arr) // 2:
                break
        return res
