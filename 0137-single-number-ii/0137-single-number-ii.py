class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(32):
            count = 0
            for num in nums:
                if num&(1<<i):
                    count += 1
                
            if count%3:
                ans |= 1<<i
                
        return ans if ans < (1<<31) else ans - (1<<32)
                