class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1
        # creating a list to append
        result = []

        # using enumerate to make nums having their indexes
        for index, number in enumerate(nums):
            # second number to match with the target
            difference = target - number

            if difference in nums[index+1]:
                result.append(index)
                result.append(nums[index+1:].index(difference)+index+1)

        return result


        # Solution 2
        
        for num1 in range(0, len(nums)):
            for num2 in range(num1+1, len(nums)):
                if nums[num1] + nums[num2] == target:
                    return [num1, num2]



        # Solution 3

        visited = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in visited:
                return [visited[difference], index]
            else:
                visited[number] = index
        return visited
