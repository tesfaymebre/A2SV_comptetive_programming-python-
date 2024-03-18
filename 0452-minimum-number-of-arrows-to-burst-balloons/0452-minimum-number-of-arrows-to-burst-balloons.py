class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        low, high = points[0][0], points[0][1]
        count = 1
        
        for i in range(1,len(points)):
            if points[i][0] <= high:
                low, high = points[i][0], min(high, points[i][1])
            else:
                low, high = points[i][0], points[i][1]
                count += 1
                
        return count