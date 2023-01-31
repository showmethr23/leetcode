class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # Solution 1
        # Find out the sum of nums indicating left and right difference as minus (current nums[i] + leftsum) from whole sum

        wholesum = sum(nums)
        leftsum = 0

        for i, n in enumerate(nums):
            if leftsum == (wholesum - leftsum - n):
                return i
            leftsum += n
        return -1

        

