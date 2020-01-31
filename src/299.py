class Solution:
    
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        a_dict1 = dict()
        a_dict2 = dict()        
        
        for i in range(len(secret)):
            s = secret[i]
            g = guess[i]
            if s == g:
                bulls += 1
            else:
                cnt = a_dict1.get(s, 0)
                a_dict1[s] = cnt + 1
   
                cnt = a_dict2.get(g, 0)
                a_dict2[g] = cnt + 1
                
        cows = 0
        for k, cnt in a_dict1.items():
            cows += min(a_dict2.get(k, 0), cnt)
        return str(bulls) + 'A' + str(cows) + 'B'
