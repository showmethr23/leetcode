class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        """
        Solution 1
        
        1. put nums1 in a Counter(), this will generate as dictionary
        2. declare an empty array as result
        3. iterate nums2 if there is an intersection between Counter object and nums2
        4. condition: if element in Counter object has same thing in nums2:
            1. result.append(intersection element)
            2. count down the Count[n]
        5. return result
        """
        
        count = Counter(nums1)
        ans = []

        for i in nums2:
            if count[i] > 0:
                ans.append(i)
                count -= 1
        return ans

        """
        Solution 2

        Using Two Pointers
        
        Assumption: nums1 and nums2 are already sorted or we should sort them out first

        1. Sort nums1 and nums2 if they are not sorted
        2. create the two pointers i and j
        3. create an empty list for answer
        4. using while loop - condition: i is less than len(nums1) and j is less than len(nums2)
            1. if - condition: nums1[i] < nums2[j]
                compare the value between nums1 and nums2 and if nums1's value is less than nums2's value
               
                i pointer goes up 
                1. i += 1 
            2. if - condition: nums1[i] > nums2[j]
                compare the value between nums1 and nums2 and if nums1's value is greater than nums2's value

                j pointer goes up
                1. j += 1
            3. else - if the both values are the same

                1. append the either nums1's or nums2's value into an answer list
                2. i += 1
                3. j += 1
        5. return an answer list
        """

        nums1, nums2 = sorted(nums1), sorted(nums2)
        i, j = 0, 0
        ans = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans


