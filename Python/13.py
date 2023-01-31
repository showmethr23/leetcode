class Solution:
    def romanToTint(self, s: str) -> int:

        # Solution 1

        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        num = 0

        # last letter cannot compare with next letter
        for i in range(0, len(s)-1):
            # if previous letter is smaller than next letter
            if dict[s[i]] < dict[s[i]]:
                # delete the letter
                num -= dict[s[i]]
            # if next letter is bigger
            else:
                # add the letter
                num += dict[s[i]]
        # add stored number + last letter
        return num + dict[s[-1]]


        # Solution 2

        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        total = 0
        
        for i in range(len(s)):
            if(i < len(s)-1):
                if (s[i] == "I" and s[i+1] == "V"):
                    total -= 1
                elif (s[i] == "I" and s[i+1] == "X"):
                    total -= 1
                elif (s[i] == "X" and s[i+1] == "L"):
                    total -= 10
                elif (s[i] == "I" and s[i+1] == "C"):
                    total -= 10
                elif (s[i] == "C" and s[i+1] == "D"):
                    total -= 100
                elif (s[i] == "I" and s[i+1] == "M"):
                    total -= 100
                else:
                    total += dict.get(s[i])
            else:
                total += dict.get(s[i])
        return total

               

