class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Example: "apple" becomes "5#apple"
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            # Find the next delimiter to get the length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            # Extract the actual string based on the length
            res.append(s[j + 1 : j + 1 + length])
            
            # Move the pointer to the start of the next length-prefix
            i = j + 1 + length
        return res
