class Solution:
    
    def minOperations(self, boxes: str) -> List[int]:
        i = 1
        accRight = 0
        notEmptyRight = 0
        LEN = len(boxes)
        while i < LEN:
            if boxes[i] == '1':
                accRight += i
                notEmptyRight += 1
            i += 1
        
        res = [accRight]
        accLeft = 0
        notEmptyLeft = 0 if boxes[0] == '0' else 1
        i = 1
        while i < LEN:
            accLeft += notEmptyLeft
            accRight -= notEmptyRight
            if boxes[i] == '1':
                notEmptyLeft += 1
                notEmptyRight -= 1
            res.append(accLeft+accRight)
            i += 1
        return res

