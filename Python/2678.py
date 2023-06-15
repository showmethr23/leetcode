class Solution:
    def countSeniors(self, details: List[str]) -> int:

        # Solution 1
        # Using counts

        res = 0

        for string in details:
            age = int(string[-4:-2])

            if age > 60:
                res += 1
        
        return res