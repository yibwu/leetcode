class Solution:
    
    def isLeapYear(self, year):
        if year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    
    def dayOfYear(self, date: str) -> int:
        nums = list(map(lambda x: int(x), date.split('-')))    
        y, m, d = nums[0], nums[1], nums[2] 
        
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear(y):
            days[1] = 29
        
        acc = 0
        for i in range(m - 1):
            acc += days[i]
        acc += d
        return acc
