class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = defaultdict(int)
        max_len = 0
        
        left = 0
        for right in range(len(s)):
            count[s[right]] += 1
            
            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1
                
                if count[s[left]] == 0:
                    del count[s[left]]
                    
            max_len = max(max_len, right - left + 1)
                
        return max_len