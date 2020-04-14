class Solution:

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        begin_x, end_x = max(rec1[0], rec2[0]), min(rec1[2], rec2[2])
        begin_y, end_y = max(rec1[1], rec2[1]), min(rec1[3], rec2[3])
        
        return (begin_x < end_x) and (begin_y < end_y)
