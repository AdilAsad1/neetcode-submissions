class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ''
        for s in strs:
            st += str(len(s)) + '#' + s
        return st

    def decode(self, s: str) -> List[str]:
        res = []
        a = 0
        while a < len(s): 
            st = ''
            b = a
            while s[b] != '#':
                b += 1
            length = int(s[a:b])
            start = b + 1
            end = start + length

            st = ''
            for i in range(start, end):
                st += s[i]

            res.append(st)
            a = end
        return res


'''
encode: len() + # + actual string
eg 5#Hello5#World

decode: read the first number and the delimiter, add the string of length of the number read in the response list. iterate until the end of the string
'''