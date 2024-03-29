class Solution:
    def climbStairs(self, n: int) -> int:
        #bottom up dp solution
        if n == 1:
            return 1
        
        pos1 = 1
        pos2 = 2
        
        for i in range(2,n):
            curr = pos1+pos2
            pos1 = pos2
            pos2 = curr
            
        return pos2
       
    """
    #top down dp solution
        memo = {}
        
        def dp(pos):
            if pos == 1:
                return 1
            elif pos == 2:
                return 2
            
            if pos in memo:
                return memo[pos]
            
            memo[pos] = dp(pos-1) + dp(pos-2)
            return memo[pos]
        
        return dp(n)
    """
    