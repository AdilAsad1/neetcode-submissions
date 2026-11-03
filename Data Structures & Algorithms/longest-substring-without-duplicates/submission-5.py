class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        longest = ''
        r = 0
        l = 0
        max_len = 0
        while r < len(s):
            if s[r] not in longest:
                longest += s[r]
                r += 1
                max_len = max(max_len, len(longest))
            else:
                duplicate_idx = longest.index(s[r])
                longest = longest[duplicate_idx + 1:]
                
        
            
        return max_len
        
