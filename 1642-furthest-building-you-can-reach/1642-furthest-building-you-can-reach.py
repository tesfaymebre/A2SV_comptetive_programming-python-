class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []
        
        for i in range(len(heights) - 1):
            
            diff = heights[i+1] - heights[i]
            
            if diff > 0:
                
                if diff <= bricks:
                    heapq.heappush(max_heap, -diff)
                    bricks -= diff
                    
                elif diff > bricks:
                    if ladders > 0:
                        ladders -= 1
                    else:
                        return i
                    
                    if max_heap and diff < (-1*max_heap[0]):
                        
                        bricks += (-1*heapq.heappop(max_heap))
                        heapq.heappush(max_heap, -diff)
                        bricks -= diff
            
        return len(heights) - 1 