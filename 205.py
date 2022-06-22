class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Solution 1
        # counting characters

        # base case
        # if strings are not having same lengths

        if len(s) != len(t):
            return False

        # better using mapping because it has the fastest speed
        for c1, c2 in zip(s, t):

            if (c1 not in mapST) and (c2 not in mapTS):
                mapST[c1] = c2
                mapTS[c2] = c1

            elif (mapST.get(c1) != c2) or (mapTS.get(c2) != c1):
                return False

        return True
