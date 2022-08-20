class Solution:
    def countSubStrings(self, s: str) -> int:

        # Solution 1

        if not s:
            return 0
        elif len(s) == 1:
            return 1

        res = 0

        for i in range(len(s)):
            res += self.countPalindrome(s, i, i)
            res += self.countPalindrome(s, i, i+1)
        return res
    

    def countPalindrome(self, s, l , r) -> int:
        res = 0

        while l >= 0 and r < len(s) and s[r] == s[l]:
            res += 1
            l -= 1
            r += 1
        return res
