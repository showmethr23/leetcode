class Solution:
    def rob(self, nums: List[int]) -> int:

        # Solution 1

        n = len(nums)

        if n == 1:
            return nums[0]
        elif not nums:
            return 0

        return max(self.rob_house(nums[1:]), self.rob_house(nums[:-1]))

    def rob_house(self, nums: List[int]) -> int:

        rob1, rob2 = 0, 0

        for current in nums:
            temp = max(rob1 +current, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
