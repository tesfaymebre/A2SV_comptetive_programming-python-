class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                ans = float('inf')
                
                for k in range(i+1,j):
                    ans = min(ans,dp(i,k)+dp(k,j)+values[i]*values[k]*values[j])
                
                if ans == float('inf'):
                    return 0
                
                memo[(i,j)] = ans
            
            return memo[(i, j)]
        return dp(0, len(values) - 1)