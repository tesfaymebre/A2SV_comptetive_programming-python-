class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        #using stack
        
        stack = [float('inf')]
        result = 0
        
        for i in range(len(arr)):
            while stack and stack[-1] <= arr[i]:
                result += stack.pop()*min(stack[-1],arr[i])
                
            stack.append(arr[i])
            
        while len(stack) > 2:
            result += stack.pop()*stack[-1]
            
        return result
        
        
        """
        #greedy approach
        result = 0
        
        while len(arr) > 1:
            idx_min = arr.index(min(arr))
            
            if 0 < idx_min < len(arr)-1:
                result += arr[idx_min]*min(arr[idx_min-1],arr[idx_min+1])
            else:
                result += arr[idx_min]*(arr[idx_min-1] if idx_min-1 != -1 else arr[idx_min+1] )
                
            arr.pop(idx_min)
            
        return result
        """
        
        """
        #bottom up dp solution
        
        size = len(arr)
        dp = [[float('inf')]*(size+1) for _ in range(size+1)]
        
        for i in range(size-1,-1,-1):
            for j in range(size):
                if j-i+1 == 2:
                    dp[i][j] = arr[i]*arr[j]
                elif j-i+1 < 2:
                    dp[i][j] = 0
                    
                for k in range(i+1,j):
                    left = dp[i][k]+dp[k+1][j]+max(arr[i:k+1])*max(arr[k+1:j+1])
                    right = dp[i][k-1]+dp[k][j]+max(arr[i:k])*max(arr[k:j+1])
                    dp[i][j] = min(dp[i][j],left,right)
                    
        return dp[0][size-1]
        """
    
        """
        #top down dp solution
        def dp(i,j):
            if (i,j) not in memo:
                
                if j-i+1 == 2:
                    return arr[i]*arr[j]
                elif j-i+1 < 2:
                    return 0
                
                ans = float('inf')
                
                for k in range(i+1,j):
                    left = dp(i,k)+dp(k+1,j)+max(arr[i:k+1])*max(arr[k+1:j+1])
                    right = dp(i,k-1)+dp(k,j)+max(arr[i:k])*max(arr[k:j+1])
                    ans = min(ans,left,right)
                    
                memo[(i,j)] = ans
                
            return memo[(i,j)]
        
        memo = {}
        
        return dp(0,len(arr)-1)
        """