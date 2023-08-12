class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # Solution 1
        # 

        n = len(nums)
        ans = []

        # base case
        if n == 0:
            return ans

        for i in range(n*2):
            ans.append(nums[i%n])

        return ans
