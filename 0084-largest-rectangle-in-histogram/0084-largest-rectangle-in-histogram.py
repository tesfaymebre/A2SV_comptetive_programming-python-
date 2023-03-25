class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = (i - stack[-1] - 1)  if stack else i
                max_area = max(max_area, h*w )
            
            stack.append(i)
        
        return max_area