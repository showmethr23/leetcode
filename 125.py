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
        # Using slicing 
        s = s.lower()

        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]
