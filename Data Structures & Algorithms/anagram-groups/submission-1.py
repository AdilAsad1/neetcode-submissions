class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            j = "".join(sorted(i))
            if j in dic:
                dic[j].append(i)
            else:
                dic[j] = [i]

        lst=[]
        for i in dic.values():
            lst.append(i)

        return lst