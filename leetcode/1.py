#Solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for index, number in enumerate(nums):
            difference = target - number

            if difference in nums[index+1]:
                result.append(index)
                result.append(nums[index+1:].index(difference)+index+1)

        return result



