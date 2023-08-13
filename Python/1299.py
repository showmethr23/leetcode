class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # Solution 1
        # Max Method

        # base case
        if len(arr) == 0:
            return arr

        rightMax = -1

        for i in range(len(arr)-1, -1, -1):
            temp = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = temp

        return arr
