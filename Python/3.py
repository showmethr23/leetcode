class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Solution 1
        # sliding windoe
        
        n = len(s)
        res = 0
        charset = set()
        l = 0
        # base case
        if n == 0:
            return 0

        if n == 1:
            return 1
        
        for r in range(n):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            
            charset.add(s[r])
            res = max(res, r - l +1)
        
        return res
