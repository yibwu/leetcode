class Solution:
    
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt = 0
        arr = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
                arr.append(i)
        if cnt == 0:
            return True
        if cnt == 1 or cnt > 2:
            return False
        
        i, j = arr[0], arr[1]
        return s1[i] == s2[j] and s1[j] == s2[i]
 
