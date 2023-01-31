class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        # Solution 1 
        # Approach -> using nested for loop to take a look at arr2 first and compare with arr1 elements
        # Crate an empty list 
        # If arr2 element exists in arr1, append it to the empty list
        # Create another list that contains arr1 elements, which are not in arr2

        ans = []

        for i in arr2:
            for j in arr1:
                if i == j:
                    ans.append(j)

        arr1_left_elements = [i for i in arr1 if i not in arr2]
        arr1_left_elements.sort()
        ans.extend(arr1_left_elements)

        return ans
        
