class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Solution 1
        # Solving with the list

        strs = []

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

        
        # Solution 2
        
        strs = []

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        return strs == strs[::-1]

        
    
        # Solution 3
        # Using Deque

        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


        # Solution 4
        # Using slicing and regular expressioni 
        s = s.lower()

        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]

        # Solution 5 
        # using two pointers

    def alphaNum(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )

        l, r = 0, len(s) + 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not slef.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        returrn True
