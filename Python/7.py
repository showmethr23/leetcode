class Solution:
    def reverse(self, x: int) -> int:
        
        # Solution 1

        # make number string and reverse it
        reverse_number = str(x)[::-1]
        if reverse_number[-1] == '-':
            new_number = int(reverse_number[-1] + reverse_number[:-1])
            return new_number
        return int(reverse_number)


        # Solution 2
        if x > 0:
            if abs(int(str(x)[::-1])) <= 2**31:
                return int(str(x)[::-1])
            else:
                return 0
        else:
            if abs(- int(str(abs(x))[::-1])) <= 2**31:
                return - int(str(abs(x))[::-1])
            else:
                return 0


