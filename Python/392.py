class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # Solution 1
        # using two-pointers

        # base case
        if len(s) < 1:
            return True
        
        if len(s) > len(t):
            return false

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == len(s):
            return True
        else:
            False

        # Solution 2
        # using counts

        # base case
        if len(s) < 1:
            return True;

        if len(s) > len(t):
            return False;

        subs = 0

        for i in range(len(t)):
            if subs <= len(s):
                if s[subs] == t[i]:
                    subs += 1

        if len(s) == subs:
            return True;

        return False;
