class Solution:
    def maxSubarray(self, nums: List[int]) -> int:

        # Solution 1

        # Idea: store the current and maximum data into variables
        # Keep updating the data whenever looping element comes

        # Base case
        if not nums:
            return 0

        # starting point is the nums[0] for current and maximum
        current = max_num = nums[0]
        
        # start looping at index 1
        for num in nums[1:]:
            
            # compare the current and current + element
            # update the data for both current and maximum number
            current = max(num, current + num)
            max_num = max(current, max_num)

        return max_num
