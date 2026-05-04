class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        a = []
        b = set(nums)
        for i in b:
            if i-1 not in b:
                a.append(i)
        
        max_len = 0
        
        for i in a:
            current = i
            count = 1

            while current + 1 in b:
                count += 1
                current += 1
            
            max_len = max(max_len, count)
    
            
        return max_len

        