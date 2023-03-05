class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_list = []
        minn = nums[0]
        
        for num in nums:
            minn = min(minn,num)
            min_list.append(minn)
            
        stack = []
        for j in range(len(nums)-1,-1,-1):
            if nums[j] > min_list[j]:
                while stack and stack[-1] <= min_list[j]:
                    stack.pop()
                    
                if stack and stack[-1] < nums[j]:
                    return True
                
                stack.append(nums[j])
            
        return False