class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        right = -1
        left = 0
        n = len(s)//2
        for i in range(n):
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
