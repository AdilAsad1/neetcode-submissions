class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        i = 0
        n = len(heights) - 1 
        while i < n:
            a = (n - i) * min(heights[i], heights[n])
            if  a > maximum:
                maximum = a
                
            if heights[i] > heights[n]:
                n -= 1
            else: 
                i += 1
        return maximum