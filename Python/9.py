class Solution:
    def is Palindrome(self, x; int) -> bool:

        # Solution 1

        num = str(x)
        if num[::-1] == num:
            return True
        return False


        # Solution 2

        return str(x)[::-1] == str(x)


        # Solution 3

        origin  = x
        reverse = 0

        # runs until num == 0
        while num > 0:
            # store reversed number until while loop ends
            reverse = (reverse * 10) + (x % 10) 
            x //= 10

        return origin == reverse
