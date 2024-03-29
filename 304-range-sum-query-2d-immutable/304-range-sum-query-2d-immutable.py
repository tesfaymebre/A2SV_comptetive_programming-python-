class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre = [[0] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for val in matrix[i]:
                self.pre[i].append(self.pre[i][-1]+val)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        
        for j in range(row1,row2+1):
            total += self.pre[j][col2+1] - self.pre[j][col1]
            
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)