class Solution:
    
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_degree = ((hour % 12) * 5 + minutes * 2.5 / 30) * 6
        minute_degree = (minutes % 60) * 6
        diff = abs(hour_degree - minute_degree)
        return diff if diff < 180 else (360 - diff)
