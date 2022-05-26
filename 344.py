class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        # Solution 1
        # Using two-pointer
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        # Solution 2
        # Pytionic way

        s.reverse()

        or

        s = s[::-1]
