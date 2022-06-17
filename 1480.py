class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # Solution 1
        #

        ans = []

        for i in range(len(nums)):
            if i = 0:
                ans.append(nums[i])

            if i >= 1:
                ans.append(nums[i] + ans[i-1])

        return ans


        # Solution 2

        ans = [nums[0]]

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            ans.append(nums[i])

        return ans
                
