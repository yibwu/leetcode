class Solution:
    
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        pos_index = 1
        neg_index = -1
        acc = 0
        s = 0
        
        for i, n in enumerate(satisfaction):
            if n > 0:
                s += n
                acc += pos_index*n
                pos_index += 1
            else:
                neg_index = i
            
        if acc == 0:
            return 0
    
        max_val = acc
        while neg_index >= 0:
            s += satisfaction[neg_index]
            acc += s
            max_val = max(max_val, acc)
            neg_index -= 1
        return max_val

