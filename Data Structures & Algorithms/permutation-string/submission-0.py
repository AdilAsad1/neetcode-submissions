class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hm1 = {}
        hm2 = {}

        for i in s1:
            hm1[i] = hm1.get(i,0) + 1

        l = 0

        for r in range(len(s2)):
            hm2[s2[r]] = hm2.get(s2[r], 0) + 1

            if r - l + 1 > len(s1):
                hm2[s2[l]] -= 1

                if hm2[s2[l]] == 0:
                    del hm2[s2[l]]

                l += 1

            if hm1 == hm2:
                return True

        return False
