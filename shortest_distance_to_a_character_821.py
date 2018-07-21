class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        INVALID = -1
        STR_LEN = len(S)
        position_c = INVALID
        result = []
        
        for i, ch in enumerate(S):
            if ch == C:
                position_c = i
                result.append(0)
            else:
                if position_c == INVALID:
                    result.append(INVALID)
                else:
                    result.append(i - position_c)
        
        position_c = INVALID
        for i, ch in enumerate(S[::-1]):
            j = STR_LEN - 1 - i
            if ch == C:
                position_c = i
            else:
                if position_c == INVALID:
                    pass
                else:
                    if result[j] == INVALID:
                        result[j] = i - position_c
                    elif result[j] > i - position_c:
                        result[j] = i - position_c
        return result
