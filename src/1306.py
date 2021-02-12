class Solution:
    
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        return self.helper(arr, start, visited)
    
    def helper(self, arr, start, visited):
        if start < 0 or start >= len(arr) or start in visited:
            return False
        if arr[start] == 0:
            return True
        visited.add(start)
        return self.helper(arr, start+arr[start], visited) or self.helper(arr, start-arr[start], visited)
        
