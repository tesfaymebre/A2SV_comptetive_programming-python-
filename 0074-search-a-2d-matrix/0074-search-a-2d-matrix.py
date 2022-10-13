class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[bisect.bisect(row,target)-1] == target:
                return True
            
        return False
            