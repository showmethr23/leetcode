class Solution:
    def search(self, nums: List[int], target: int) -> int:


        # Solution 1
        # Binary search algorithm

        l, r = 0, len(nums) -1

        while l <= r:

            mid = (l+r) // 2

            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < numd[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

