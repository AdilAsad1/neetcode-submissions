class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for i in strs:
            s = sorted(i)
            k = str(s)
            if k not in d:
                d[k] = [i]
            else:
                d[k].append(i)

        return list(d.values()) 
