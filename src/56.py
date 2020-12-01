class Solution:
    
    def isOverlap(self, point1, point2):
        return point1[1] >= point2[0]
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        i = 0
        while i < len(intervals) - 1:
            if self.isOverlap(intervals[i], intervals[i+1]):
                new_interval = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])]
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, new_interval)
            else:
                i += 1
        return intervals

