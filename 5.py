class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Solution 1
        # Using two-pointer for expanding from the middle

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        # If there is no application then return
        if len(s) < 2 or s == 2[::-1]:
            return s

        result = ''

        # Sliding
        for i in range(len(s) -1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result
