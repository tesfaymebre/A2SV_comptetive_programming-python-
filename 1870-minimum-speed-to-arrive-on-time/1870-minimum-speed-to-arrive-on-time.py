class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        upper = max(max(dist), ceil(dist[-1] / 0.01))
        
        total = lambda speed: sum(map(lambda x: ceil(x / speed), dist[:-1])) + (dist[-1] / speed)
        if total(upper) > hour:
            return -1
        
        left, right = 1, upper
        while left < right:            
            mid = left + (right - left) // 2
            if total(mid) > hour:
                left = mid + 1 # should be larger
            else:
                right = mid # should explore a smaller one
        return right