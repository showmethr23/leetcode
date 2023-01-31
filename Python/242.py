class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Solution 1

        if len(s) != len(t) or not s or not t:
            return False

        if sorted(s) == sorted(t):
            return True
        else:
            return False


        # Solution 2

        countS, countT = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(t[i], 0):
                return False

        return True
