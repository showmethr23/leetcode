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

        # Solution 2
        # DP, Expanding from middle

        if len(s) == 1:
            return s
        elif not s:
            return 0
        elif len(s) == 2 and s[-1] == s[0]:
            return s

        res = ""
        resLen = 0

        # we will see every position in the string
        for i in range(len(s)):

            # odd length

            l, r = i, i
            # Iterate until if two pointers are inbound within the string and are palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                # if they are palindome and longer than previous updated answer
                if (r - l + 1) > resLen:

                    # Update a answer and answer length
                    res = s[l:r+1]
                    resLen = r - l + 1

                # expand the pointers left and right
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                l -= 1
                r += 1
        return res
