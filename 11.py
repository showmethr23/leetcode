class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Solution 1
        # using two pointers

        # base case
        if len(height) < 2:
            return 0

        max_area = 0
        l, r = 0, len(height)-1

        while l < r:

            max_area = max(max_area, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return max_area
