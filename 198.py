class Solution:
    def rob(self, nums: List[int]) -> int:

        # Solution 1
        # DP

        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

        # Solution 2
        # Easier to understand

        if len(nums) == 1:
            return nums[0]

        if not nums:
            return 0

        dp = [0 for i in range(0, len(nums))]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-2])

        return dp[-1]


