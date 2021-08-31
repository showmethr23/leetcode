class Solution:
    def reverse(self, x: int) -> int:
        
        # Solution 1

        # make number string and reverse it
        reverse_number = str(x)[::-1]
        if reverse_number[-1] == '-':
            new_number = int(reverse_number[-1] + reverse_number[:-1])
            return new_number
        return int(reverse_number)





