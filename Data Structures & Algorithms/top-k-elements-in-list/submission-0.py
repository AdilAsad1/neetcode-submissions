class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        # Sort the dictionary items by frequency (value) in descending order
        sorted_elements = sorted(d.items(), key=lambda x: x[1], reverse=True)
        
        # Return the first k elements
        return [item[0] for item in sorted_elements[:k]]