class Solution:
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        i = 1
        cnt = 0
        LEN = len(flowerbed)
        
        while i < LEN - 1:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                cnt += 1
            i += 1
        return cnt >= n

