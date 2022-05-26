class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Solution 1

        if not nums or len(nums) < 2:
            return False

        dict = {}

        for i in nums:
            if i in dict:
                return True
            else:
                dict[i] = 1
        return False

        # Solution 2
        # count the elements

        count = 0
        for i in range(len(nums)):
            count += 1

        ans = set(nums)

        if count > len(ans):
            return True
        else:
            return False

        # Solution 3
        # Sort the array and compare next elements

        ans = sorted(nums)
        
        for i in range(len(ans)-1):
            if ans[i] == ans[i+1]:
                return True
            else:
                return False

